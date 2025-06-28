import subprocess
import os
import glob

def setup_audio():
    packages = [
        'sof-firmware',
        'alsa-ucm-conf',
        'alsa-utils',
        'pipewire',
        'pipewire-audio',
        'pavucontrol',
        'plasma-pa'
    ]

    # Установка пакетов с sudo
    print('🔄Установка необходимых пакетов пакетов')
    try :
        subprocess.run(['sudo', 'pacman', '-S', '--noconfirm'] + packages)
        print("✅ Успешно установлено")
    except subprocess.CalledProcessError:
        print('❌ Ошибка установки')

    #Загрузка модуля ядра
    print('🔄Загрузка модуля ядра')
    try :
        subprocess.run(['sudo', 'modprobe', 'snd_sof_amd_renoir'])
        print("✅ Успешно")
    except subprocess.CalledProcessError as ex:
        print('❌ Ошибка установки\n' + ex)

    # Запуск аудиослужб в пользовательской сессии
    services = [
        'pipewire', 
        'pipewire-pulse', 
        'wireplumber'
    ]

    print('🔄Добавление служб в systemd')
    try :
        subprocess.run(['systemctl', '--user', 'enable', '--now'] + services)
        print("✅ Успешно")
    except subprocess.CalledProcessError as ex:
        print('❌ Ошибка systemd\n' + ex)

    #Настройка кнопок регултровки громкости
    print('🔄Настройка кнопок регултровки громкости')
    for path in glob.glob(os.path.expanduser("~/.cache/plasma*")):
        try:
            os.remove(path)
        except Exception:
            pass

    try:
        os.remove(os.path.expanduser("~/.config/plasma-org.kde.plasma.desktop-appletsrc"))
    except Exception:
        pass

    subprocess.run(["killall", "plasmashell"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen(["plasmashell", "--replace"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    #Копирование конфига grub
    print("\n> Копирование grub.cfg в /etc/default/")
    try:
        subprocess.run(['sudo', 'cp', 'config/grub.cfg', '/etc/default/'])
        print("✅ Файл скопирован успешно")
    except Exception as e:
        print(f"❌ Ошибка при копировании: {e}")
