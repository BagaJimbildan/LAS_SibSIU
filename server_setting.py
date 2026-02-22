import subprocess

def disconnect_server():
    subprocess.run(f'net use Z: /delete', shell=True)