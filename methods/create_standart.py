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