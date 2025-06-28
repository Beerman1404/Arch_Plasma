import subprocess
import os
import glob

def run_command(command, use_sudo=False):
    if use_sudo:
        command = ['sudo'] + command
    print(f"\n> Выполняется: {' '.join(command)}")
    try:
        subprocess.run(command, check=True)
        print("✅ Успешно")
    except subprocess.CalledProcessError:
        print("❌ Ошибка выполнения команды")

def main():
    # Установка пакетов с sudo
    packages = [
        'sof-firmware',
        'alsa-ucm-conf',
        'alsa-utils',
        'pipewire',
        'pipewire-audio',
        'pavucontrol',
        'plasma-pa',
        'plasma-nm'
    ]
    run_command(['pacman', '-S', '--noconfirm'] + packages, use_sudo=True)

    #Загрузка модуля ядра
    run_command(['modprobe', 'snd_sof_amd_renoir'], use_sudo=True)
    
    # Запуск аудиослужб в пользовательской сессии
    services = ['pipewire', 'pipewire-pulse', 'wireplumber']
    run_command(['systemctl', '--user', 'enable', '--now'] + services, use_sudo=True)

    #Настройка кнопок регултровки громкости
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

    print(f"\n> Копирование {filename} в /etc/default/")
    try:
        run_command(['cp', '.config/grub.cfg', '/etc/default/'], use_sudo=True)
        print("✅ Файл скопирован успешно")
    except Exception as e:
        print(f"❌ Ошибка при копировании: {e}")

if __name__ == '__main__':
    main()
