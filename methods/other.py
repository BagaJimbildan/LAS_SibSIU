import platform
import subprocess
import static_info as stat_inf


def ping(host: str, timeout = 4):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    if stat_inf.os.lower() == 'windows':
        command = ['ping', param, '1', '-w', str(timeout * 1000), host]
    else:
        command = ['ping', param, '1', '-W', str(timeout), host]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=timeout
    )
    return result.returncode == 0