import ctypes
import platform
import re
import subprocess



import static_info as stat_inf
import key_phrases as k_phras

if platform.system().lower() == "windows":
    import winreg



def check_system():
    # Проверка системы
    stat_inf.os = platform.system()
    stat_inf.platform = platform.platform()



def check_domain():
    # Проверка домена
    if stat_inf.os.lower() == "windows":

        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters") as key:
            stat_inf.domain, _ = winreg.QueryValueEx(key, "Domain")
    elif stat_inf.os.lower() == "linux":
        stat_inf.domain = "пока не знаю linux"

    if stat_inf.domain == "":
        stat_inf.domain = "нет"

def check_activate():
    if stat_inf.os.lower() == "windows":
        # Открываем ключ реестра с основной информацией о системе
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

        # Пробуем прочитать несколько значений, связанных с активацией
        try:
            # Читаем значение DigitalProductId (если существует, обычно означает активацию)
            winreg.QueryValueEx(key, "DigitalProductId")
            stat_inf.activate = k_phras.activate_status[0]

        except:
            try:
                # Читаем значение ProductId
                winreg.QueryValueEx(key, "ProductId")
                stat_inf.activate = k_phras.activate_status[0]
            except:
                try:
                    # Проверяем специальный ключ активации
                    key_activation = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                                    r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform")
                    activation_value, type = winreg.QueryValueEx(key_activation, "Activation")
                    winreg.CloseKey(key_activation)

                    if activation_value == 1:
                        stat_inf.activate = k_phras.activate_status[0]
                    else:
                        stat_inf.activate = k_phras.activate_status_no[0]
                except:
                    stat_inf.activate = "???"

        # Закрываем основной ключ
        winreg.CloseKey(key)

    elif stat_inf.os.lower() == "linux":
        stat_inf.activate = stat_inf.os.lower()

def check_dhcp():
    if stat_inf.os.lower() == "windows":
        result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True, encoding="cp866")
        lines = result.stdout.split('\n')

        in_ethernet_section = False

        for line in lines:
            line = line.strip()

            # Проверяем, начинается ли секция Ethernet адаптера
            if k_phras.adapter_ethernet[0] in line.lower() or k_phras.adapter_ethernet[1] in line.lower():
                in_ethernet_section = True
                continue

            # Если мы внутри секции Ethernet адаптера, ищем строку с DHCP
            if in_ethernet_section:
                # Если нашли DHCP - извлекаем статус
                if "DHCP включен" in line:
                    status = k_phras.enabled[0] if "Да" in line else k_phras.enabled_no[0]
                    stat_inf.dhcp = status
                    break  # Прерываем цикл после нахождения статуса для Ethernet

                # Если встречаем начало другого адаптера - выходим из секции Ethernet
                if "адаптер" in line.lower() and "ethernet" not in line.lower():
                    in_ethernet_section = False

    elif stat_inf.os.lower() == "linux":
        stat_inf.dhcp = "не знаю linux"

def check_network():
    if stat_inf.os.lower() == "windows":
        result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True, encoding="cp866")
        lines = result.stdout.split('\n')

        in_ethernet_section = False
        in_dns_section = False

        for line in lines:

            if in_dns_section:
                dns_matches = re.findall(r'(\d+\.\d+\.\d+\.\d+)', line)
                if dns_matches:
                    stat_inf.net_dns[1] = dns_matches[0]
            in_dns_section = False
            line = line.strip()

            # Находим Ethernet адаптер
            if k_phras.find_phras(line, k_phras.adapter_ethernet):
                in_ethernet_section = True
                continue

            if in_ethernet_section:
                # IP адрес
                if "ipv4-адрес" in line.lower() and stat_inf.net_ip_addr == stat_inf.do_not_know:
                    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        stat_inf.net_ip_addr = match.group(1)

                # Маска подсети
                elif "маска подсети" in line.lower() and stat_inf.net_mask == stat_inf.do_not_know:
                    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        stat_inf.net_mask = match.group(1)

                # Шлюз
                elif "основной шлюз" in line.lower() and stat_inf.net_gateway == stat_inf.do_not_know:
                    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        stat_inf.net_gateway = match.group(1)

                # DNS
                elif "dns-серверы" in line.lower() and stat_inf.net_dns[0] == stat_inf.do_not_know:
                    dns_matches = re.findall(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if dns_matches:
                        stat_inf.net_dns[0] = dns_matches[0]
                        in_dns_section = True


def check_admin_on():
    if stat_inf.os.lower() == "windows":
        try:
            result = subprocess.run(
                ["net", "user", "Администратор"],
                capture_output=True,
                text=True,
                encoding='cp866'
            )
            lines = result.stdout.split('\n')
            for line in lines:
                if "учетная запись активна" in line.lower():
                    if k_phras.find_phras(line, k_phras.ans_yes): stat_inf.admin_active = k_phras.enabled[1]
                    elif k_phras.find_phras(line, k_phras.ans_no): stat_inf.admin_active = k_phras.enabled_no[1]
                    else: "???"
        except Exception as e:
            print(f"Ошибка: {e}")

    elif stat_inf.os.lower() == "linux":
        stat_inf.admin_active = "стандарт linux на администратора неизвестен"

def check_status_current_user():
    # Возвращает от админа ли запущена программа: 1 - да, 0 - нет

    if stat_inf.os.lower() == "windows":
        stat_inf.admin_current_user =  ctypes.windll.shell32.IsUserAnAdmin()
    elif stat_inf.os.lower() == "linux":
        stat_inf.admin_current_user = "пока не знаю linux"

def check_name():
    if stat_inf.os.lower() == "windows":
        stat_inf.name_PC = platform.node()

def check_name_standard():
    pattern = r'^[a-zA-Z0-9]+-\d{5}-[cCnNpP]$'
    matching = bool(re.match(pattern, stat_inf.name_PC))
    stat_inf.name_PC_standard = k_phras.matching_yes[0] if matching else k_phras.matching_no[0]


