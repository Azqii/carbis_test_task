import os

from httpx import HTTPStatusError

from .wrapper import DadataAPIWrapper


def clear() -> None:
    """Очищает консоль"""
    os.system("cls" if os.name == "nt" else "clear")


def pause() -> None:
    """Приостанавливает выполнение программы до нажатия клавиши Ввод"""
    input("(Нажмите Ввод для продолжения)")


def get_choice() -> int:
    """Возвращает номер выбранного пункта"""
    try:
        choice = int(input("Введите номер пункта для выбора: "))
    except ValueError:
        choice = 100
    return choice


def language_settings(api: DadataAPIWrapper):
    """Смена языка возвращаемых ответов"""
    clear()
    print("Выберите язык:")
    print("1. Русский")
    print("2. English")
    print("0. Назад\n")

    choice = get_choice()
    if choice == 1:
        api.change_language("ru")
    elif choice == 2:
        api.change_language("en")
    elif choice == 0:
        return
    else:
        print("Данного пункта нет в меню")
        pause()


def settings(api: DadataAPIWrapper):
    """Настройки"""
    while True:
        clear()
        print("Настройки:")
        print(f"API-Ключ: {api.settings.api_key} | Язык ответов: {api.settings.language.value}\n")
        print("1. Изменить API-Ключ")
        print("2. Изменить язык возвращаемых ответов")
        print("0. Назад\n")

        choice = get_choice()
        if choice == 1:
            clear()
            api_key = input("Введите новый API-Ключ: ")
            api.change_api_key(api_key)
        elif choice == 2:
            language_settings(api)
        elif choice == 0:
            break
        else:
            print("Данного пункта нет в меню. Попробуйте еще раз")
            pause()


def print_coordinates(api: DadataAPIWrapper) -> None:
    """Находит координаты нужного адреса"""
    clear()
    query = input("Введите желаемый адрес для того, чтобы узнать его координаты:\n")
    try:
        values = api.suggest(query=query)
    except HTTPStatusError:
        print("Что-то пошло не так. Вероятно, ваш API-Ключ указан неправильно.")
        pause()
        return
    clear()
    print("Возможные адреса:")
    for serial, value in enumerate(values, 1):
        print(f"{serial}. {value['value']}")
    print()

    # Делаю уточняющий запрос, как говорится в задании и документации, хотя для разгрузки сети
    # координаты можно было вытащить и из ответа на прошлый запрос.
    number = get_choice()
    try:
        address = api.suggest(query=values[number-1]["unrestricted_value"], count=1)[0]
    except IndexError:
        print("В списке нет такого пункта. Попробуйте еще раз")
        pause()
        return
    clear()
    print(f"Адрес: {address['value']}")
    print(f"Координаты: {address['data']['geo_lat']}(широта), {address['data']['geo_lon']}(долгота)")
    pause()


def menu() -> None:
    """Главное меню"""
    api = DadataAPIWrapper()
    if not api.settings.api_key:
        api_key = input("У вас не указан API-ключ, введите его: ")
        api.change_api_key(api_key)

    while True:
        clear()
        print("Меню:\n")
        print("1. Получить координаты адреса")
        print("2. Настройки")
        print("0. Выход\n")

        choice = get_choice()
        if choice == 1:
            print_coordinates(api)
        elif choice == 2:
            settings(api)
        elif choice == 0:
            break
        else:
            print("Данного пункта нет в меню. Попробуйте еще раз")
            pause()
