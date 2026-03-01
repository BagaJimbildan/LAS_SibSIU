import subprocess
import platform
import sys

def is_ping_successful(host, timeout=2):
    """
    Проверяет доступность хоста с помощью ping.

    Параметры:
        host (str): Адрес узла (например, 'ya.ru').
        timeout (int): Таймаут в секундах.

    Возвращает:
        bool: True если узел доступен, иначе False.
    """
    # Определяем параметры для разных ОС
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Формируем команду: количество запросов и таймаут
    if platform.system().lower() == 'windows':
        # Для Windows: -n 1 -w timeout (таймаут в миллисекундах)
        command = ['ping', param, '1', '-w', str(timeout * 1000), host]
    else:
        # Для Linux/Mac: -c 1 -W timeout (таймаут в секундах)
        command = ['ping', param, '1', '-W', str(timeout), host]

    try:
        # Запускаем процесс, подавляем вывод, проверяем код возврата
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=timeout + 2  # небольшой запас на выполнение
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False
    except Exception:
        return False

# Пример использования
if __name__ == '__main__':
    host = 'ad1'
    if is_ping_successful(host):
        print(f'{host} доступен')
    else:
        print(f'{host} недоступен')