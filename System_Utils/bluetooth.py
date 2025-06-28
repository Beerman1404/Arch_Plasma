import subprocess

def setup_bluetooth():
    packages = [
        'bluez',
        'bluez-utils',
        'bluedevil',
        'bluez-qt'
    ]

    #Загрузка пакетов
    print('🔄Установка пакетов : bluez bluez-util bluedevil bluez-qt')
    try :
        subprocess.run(['sudo', 'pacman', '-Syu', '--noconfirm'] + packages)
        print('✅Устанвленно успешно')
    except subprocess.CalledProcessError:
        print('❌ Ошибка установки')


    #Добавление в автозапуск
    print('🔄Добавление в автозапуск')
    try :
        subprocess.run(['sudo', 'systemctl', 'enable', 'bluetooth.service', '--now'])
        print('✅Добавленно успешно')
    except subprocess.CalledProcessError:
        print('❌ Ошибка добавления службы в systemd')
