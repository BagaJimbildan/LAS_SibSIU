import platform
import re
import subprocess
import winreg

import static_info as stat_inf
import key_phrases as k_phras


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
        stat_inf.domain = "пока не знаю"

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
            stat_inf.activate = "активировано"

        except:
            try:
                # Читаем значение ProductId
                winreg.QueryValueEx(key, "ProductId")
                stat_inf.activate = "активировано"
            except:
                try:
                    # Проверяем специальный ключ активации
                    key_activation = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                                    r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform")
                    activation_value, type = winreg.QueryValueEx(key_activation, "Activation")
                    winreg.CloseKey(key_activation)

                    if activation_value == 1:
                        stat_inf.activate = "активировано"
                    else:
                        stat_inf.activate = " не активировано"
                except:
                    stat_inf.activate = "не удалось определить"

        # Закрываем основной ключ
        winreg.CloseKey(key)

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
                    status = "включен" if "Да" in line else "выключен"
                    stat_inf.dhcp = status
                    break  # Прерываем цикл после нахождения статуса для Ethernet

                # Если встречаем начало другого адаптера - выходим из секции Ethernet
                if "адаптер" in line.lower() and "ethernet" not in line.lower():
                    in_ethernet_section = False

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
            if k_phras.adapter_ethernet[0] in line.lower() or k_phras.adapter_ethernet[1] in line.lower():
                in_ethernet_section = True
                continue

            if in_ethernet_section:
                # IP адрес
                if "ipv4-адрес" in line.lower():
                    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        stat_inf.net_ip_addr = match.group(1)

                # Маска подсети
                elif "маска подсети" in line.lower():
                    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        stat_inf.net_mask = match.group(1)

                # Шлюз
                elif "основной шлюз" in line.lower():
                    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        stat_inf.net_gateway = match.group(1)

                # DNS
                elif "dns-серверы" in line.lower():
                    dns_matches = re.findall(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if dns_matches:
                        stat_inf.net_dns[0] = dns_matches[0]
                        in_dns_section = True

                # Выходим при обнаружении другого адаптера
                if "адаптер" in line.lower() and "ethernet" not in line.lower():
                    break