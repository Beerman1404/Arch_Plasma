import subprocess

def setup_wifi_icon():
    print("🔄Установка plasma-nm")
    try :
        subprocess.run(['sudo', 'pacman', '-Syu', '--noconfirm', 'plasma-nm'])
        print("✅Успешно установлено")
    except subprocess.CalledProcessError:
        print('❌ Ошибка установки')
