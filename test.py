import subprocess
import getpass

# Данные для присоединения к домену
domain_name = "example.com"  # Замените на имя вашего домена
admin_user = "admin_user"    # Пользователь с правами в домене
admin_password = 'hjkh'
computer_name = subprocess.run(["hostname"], capture_output=True,
            text=True,
            encoding='cp866',
            check=True).stdout.strip()

# Формирование команды для присоединения к домену

# Вариант 2: Использование PowerShell (рекомендуется для Windows 10/11)
powershell_command = (
    f"Add-Computer -DomainName {domain_name} "
    f"-Credential (New-Object System.Management.Automation.PSCredential "
    f"('{admin_user}', (ConvertTo-SecureString '{admin_password}' -AsPlainText -Force))) "
    f"-Restart"
)


# Или через PowerShell
try:
    result = subprocess.run(
        ["powershell", "-Command", powershell_command],
        capture_output=True,
        text=True,
        encoding='cp866',
        check=True
    )
    print(f"Успешно: {result.stdout}")
except subprocess.CalledProcessError as e:
    print(f"Ошибка PowerShell: {e.stderr}")