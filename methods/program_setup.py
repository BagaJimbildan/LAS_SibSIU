import os
import subprocess

import static_info as stat_inf

def setup_program(parent, name, stat_inf_ref):
    path = stat_inf_ref[1]

    # Папка, где лежит программа
    program_dir = os.path.dirname(path)

    if path != stat_inf.not_selected:
        subprocess.run([path], cwd=program_dir)
    else:
        parent.dialog_error_show(f"{name} не указан")