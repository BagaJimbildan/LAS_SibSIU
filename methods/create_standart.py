import subprocess

from PyQt6.QtWidgets import QPushButton, QLabel

import static_info as stat_inf

import key_phrases as k_phras


def enable_admin(
        label_admin: QLabel , # информация в окне включена ли учетная запись админа
        btn_admin : QPushButton): # кнопка включения админки

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

        return [0, 0]

    except subprocess.CalledProcessError as e:
        return [1, e.stderr]

def pass_admin(new_password):
    try:
        subprocess.run(
            ["net", "user", "Администратор", new_password],
            check=True,
            capture_output=True,
            text=True,
            encoding='cp866'
        )
        return [0,0]

    except subprocess.CalledProcessError as e:
        return [1, e.stderr]

def rename_PC(new_name):  # имя ПК в окне

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
            return [0, 0]

        except subprocess.CalledProcessError as e:
            return [1, e.stderr]
    else:
        return [1, "не знаю пока как Linux"]

def edit_network(new_ip: list[str]):
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

            return [0,0]

        except subprocess.CalledProcessError as e:
            return [1, e.stderr.decode('cp866', errors='ignore')]
    else:
        return [1, "не знаю пока как Linux"]

def disable_user(username: str):
    try:
        subprocess.run(
            ['net', 'user', username, '/active:no'],
            capture_output=True,
            text=True,
            encoding='cp866',
            check=True
        )

        return [0,0]

    except subprocess.CalledProcessError as e:
        return [1, e.stderr]