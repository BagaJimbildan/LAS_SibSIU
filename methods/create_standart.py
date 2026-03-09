import subprocess
import threading

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

def activate_windows(error_server_show, method_update, lbl_update: QLabel):
    subprocess.run(r'slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX', shell=True)
    subprocess.run(r'slmgr.vbs /skms lic.sibsiu.ru', shell=True)
    subprocess.run(r'slmgr.vbs /ato', shell=True)

    threading.Timer(10.0,
                    lambda: update_info_activation(error_server_show, method_update, False)).start()
    lbl_update.setText("проверка активации, 10 секунд")



def activate_office(error_server_show, method_update, lbl_update):
    if stat_inf.office_installed:
        subprocess.run(r'cscript "C:\Program Files (x86)\Microsoft Office\Office14\ospp.vbs" /sethst:10.252.253.10', shell=True)
        subprocess.run(r'cscript "C:\Program Files (x86)\Microsoft Office\Office14\ospp.vbs" /act"', shell=True)

        threading.Timer(10.0,
                        lambda: update_info_activation(error_server_show, method_update, True)).start()
        lbl_update.setText("проверка активации, 10 секунд")


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
    status2 = serv_log.write_excel(action, note, True)
    if status2[0] == 2:
        dialog_error_server_show(status2[1], True)

def update_info_activation(error_server_show, method_update, is_office):
    method_update()
    try_write_server(error_server_show, "активация Office" if is_office else "активация Windows")

def sync_time(error_server_show = None):
    ok, err = run_cmd(['w32tm', '/resync'])
    if not ok:
        return [1, f"Ошибка синхронизации времени: {err}"]

    if error_server_show is not None:
        try_write_server(error_server_show, "Синхронизация времени")
    return [0, 0]

def set_time(error_server_show):
    # 1. Установка часового пояса
    ok, err = run_cmd(['tzutil', '/s', k_phras.hour_zone[0]])
    if not ok:
        return [1, f"Ошибка установки часового пояса: {err}"]

    # 2. Настройка службы времени
    ok, err = run_cmd(['sc', 'config', 'w32time', 'start=', 'auto'])
    if not ok:
        return [1, f"Ошибка настройки службы: {err}"]

    # Запуск службы (если уже запущена – ошибка игнорируется)
    subprocess.run(['net', 'start', 'w32time'], capture_output=True)

    # 3. Установка NTP-серверов
    ok, err = run_cmd(['w32tm', '/config', '/syncfromflags:manual', '/manualpeerlist:pool.ntp.org', '/update'])
    if not ok:
        return [1, f"Ошибка настройки NTP: {err}"]

    # 4. Принудительная синхронизация
    status = sync_time()
    if status[0] == 1:
        return [1, status[1]]

    # Всё выполнено успешно
    try_write_server(error_server_show, "Настройка времени")
    return [0,0]


# Хороший метод для выполнения всех запуска cmd, но пока используется только для времени
def run_cmd(command):
    try:
        subprocess.run(command, check=True, capture_output=True, text=True, encoding='cp866')
        return True, None
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip() or str(e)
