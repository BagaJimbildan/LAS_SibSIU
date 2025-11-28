import subprocess

from PyQt6.QtWidgets import QPushButton, QLabel

import key_phrases


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
        label_admin.setText(key_phrases.enabled[1])
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