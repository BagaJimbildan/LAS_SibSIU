import winreg

def get_installed_software():
    software_list = []
    # Пути к реестру, где обычно хранятся записи об установленных программах
    reg_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]
    # Также можно добавить HKEY_CURRENT_USER, если нужно
    for reg_path in reg_paths:
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_READ)
            for i in range(winreg.QueryInfoKey(reg_key)[0]):  # количество подразделов
                subkey_name = winreg.EnumKey(reg_key, i)
                subkey = winreg.OpenKey(reg_key, subkey_name)
                try:
                    name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    version = winreg.QueryValueEx(subkey, "DisplayVersion")[0] if "DisplayVersion" in [winreg.EnumValue(subkey, j)[0] for j in range(winreg.QueryInfoKey(subkey)[1])] else "N/A"
                    software_list.append({"name": name, "version": version})
                except FileNotFoundError:
                    # DisplayName отсутствует – пропускаем
                    pass
                finally:
                    subkey.Close()
            reg_key.Close()
        except FileNotFoundError:
            pass
    return software_list

if __name__ == "__main__":
    programs = get_installed_software()
    for prog in programs:
        print(f"{prog['name']} - {prog['version']}")
    print(f"Всего найдено: {len(programs)}")