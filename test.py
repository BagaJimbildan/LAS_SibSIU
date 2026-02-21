import subprocess

def mount_share_windows(drive_letter, share_path, username, password):
    cmd = f'net use {drive_letter}: {share_path} /user:{username} {password} /persistent:no'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Папка {share_path} подключена как диск {drive_letter}:")
        # После подключения можно работать с файлами через drive_letter:
        # os.listdir(f"{drive_letter}:\\")
    else:
        print("Ошибка подключения:", result.stderr)

# Пример использования
mount_share_windows('Z', r'\\ad1\share', 'hihi', '111111')