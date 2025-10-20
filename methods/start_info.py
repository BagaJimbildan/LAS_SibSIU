import platform
import subprocess
import winreg

import static_info as stat_inf


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

        for line in lines:
            line = line.strip()

            # Ищем строку с DHCP
            if "DHCP включен" in line:
                status = "включен" if "Да" in line else "выключен"
                stat_inf.dhcp = status