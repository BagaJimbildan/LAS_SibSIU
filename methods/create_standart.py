import subprocess

from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit

import static_info as stat_inf
import methods.server_logs as serv_log
import app_info as app_inf
import key_phrases as k_phras


def enable_admin(
        label_admin: QLabel , # информация в окне включена ли учетная запись админа
        btn_admin : QPushButton,  # кнопка включения админки
        error_server_show):

    try:
        subprocess.run(
            ["net", "user", "Администратор", "/active:yes"],
            check=True,
            capture_output=True,
            text=True,
            encoding='cp866'
        )

        # Если успешно:
        label_admin.setText(k_phras.enabled[1])
        stat_inf.admin_active = k_phras.enabled[1]
        btn_admin.setEnabled(False)

        try_write_server(error_server_show, "включение учетной записи администратора")

        return [0, 0]

    except subprocess.CalledProcessError as e:
        return [1, e.stderr]

def pass_admin(new_password, error_server_show):
    try:
        subprocess.run(
            ["net", "user", "Администратор", new_password],
            check=True,
            capture_output=True,
            text=True,
            encoding='cp866'
        )

        try_write_server(error_server_show, "изменение пароля администратора")

        return [0,0]

    except subprocess.CalledProcessError as e:
        return [1, e.stderr]

def rename_PC(new_name,  # имя ПК в окне
              error_server_show):

    if stat_inf.os.lower() == "windows":
        try:
            ps_script = f'Rename-Computer -NewName "{new_name}" -Force'

            subprocess.run(
                ["powershell", "-Command", ps_script],
                check=True,
                capture_output=True,
                text=True,
                encoding='cp866'
            )

            try_write_server(error_server_show, "изменение имени ПК", new_name)

            return [0, 0]

        except subprocess.CalledProcessError as e:
            return [1, e.stderr]
    else:
        return [1, "не знаю пока как Linux"]

def edit_network(new_ip: list[str], error_server_show):
    if stat_inf.os.lower() == "windows":
        try:
            cmd_ip = [
                "netsh", "interface", "ip", "set", "address",
                f"name={stat_inf.net_interface}",
                "source=static",
                f"addr={".".join(new_ip)}",
                f"mask=255.255.255.0", # надо из k_prhas брать и dnsы
                f"gateway={".".join(new_ip[0:-1]) + ".254"}"
            ]

            # Устанавливаем основной DNS
            cmd_dns1 = [
                "netsh", "interface", "ip", "set", "dns",
                f"name={stat_inf.net_interface}",
                "source=static",
                f"addr=10.252.253.1"
            ]

            cmd_dns2 = [
                "netsh", "interface", "ip", "add", "dns",
                f"name={stat_inf.net_interface}",
                f"addr=10.252.253.2",
                "index=2"
            ]

            subprocess.run(cmd_ip, check=True, capture_output=True)
            subprocess.run(cmd_dns1, check=True, capture_output=True)
            subprocess.run(cmd_dns2, check=True, capture_output=True)

            try_write_server(error_server_show, "изменение сети ПК", f"{".".join(new_ip)}")

            return [0,0]

        except subprocess.CalledProcessError as e:
            return [1, e.stderr.decode('cp866', errors='ignore')]
    else:
        return [1, "не знаю пока как Linux"]

def disable_user(username: str, error_server_show):
    try:
        subprocess.run(
            ['net', 'user', username, '/active:no'],
            capture_output=True,
            text=True,
            encoding='cp866',
            check=True
        )

        try_write_server(error_server_show, "отключение начального администратора", username)

        return [0,0]

    except subprocess.CalledProcessError as e:
        return [1, e.stderr]

def connect_domain(domain_name: str, admin_user: str, admin_password: str, error_server_show):

    powershell_command = (
        f"Add-Computer -DomainName {domain_name} "
        f"-Credential (New-Object System.Management.Automation.PSCredential "
        f"('{admin_user}', (ConvertTo-SecureString '{admin_password}' -AsPlainText -Force))) "
    )

    try:
        subprocess.run(
            ["powershell", "-Command", powershell_command],
            capture_output=True,
            text=True,
            encoding='cp866',
            check=True
        )

        try_write_server(error_server_show, "отключение начального администратора", "domain: "+domain_name+", user: "+admin_user)

        return [0, "Ввод в домен успешен + '\n' + Необходимо перезагрузить компьютер"]
    except subprocess.CalledProcessError as e:
        return [1, e.stderr]

def activate_windows(error_server_show):
    subprocess.run(r'slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX', shell=True)
    subprocess.run(r'slmgr.vbs /skms lic.sibsiu.ru', shell=True)
    subprocess.run(r'slmgr.vbs /ato', shell=True)

    try_write_server(error_server_show, "активация Windows")


def activate_office(error_server_show):
    subprocess.run(r'cscript "C:\Program Files (x86)\Microsoft Office\Office14\ospp.vbs" /sethst:10.252.253.10', shell=True)
    subprocess.run(r'cscript "C:\Program Files (x86)\Microsoft Office\Office14\ospp.vbs" /act"', shell=True)
    subprocess.run(r'pause', shell=True)

    try_write_server(error_server_show, "активация Office")

def check_tb_null(text: str):
    if text is None or text.strip() == "":
        return 1
    else:
        return 0

def try_write_server(dialog_error_server_show, action: str, note = None):
    if app_inf.write_server:
        status = serv_log.write_excel(action, note)

        if status[0] == 2:
            dialog_error_server_show(status[1])

    # Запись в локальные логи текущей сессии
    pass