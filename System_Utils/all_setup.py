from audio import setup_audio
from bluetooth import setup_bluetooth
from wifi import setup_wifi_icon

def main():

    print("🔄НАСТРОЙКА ЗВУКА")
    setup_audio()

    print("🔄НАСТРОЙКА BLUETOOTH")
    setup_bluetooth()

    print("🔄ДОБАВЛЕНИЕ ИКОНКИ WiFi")
    setup_wifi_icon()

if __name__ == "__main__":
    main()