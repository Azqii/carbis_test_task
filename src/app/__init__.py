from .db import create_db_if_doesnt_exist


def start():
    create_db_if_doesnt_exist()

    # Если импортировать раньше, а таблица еще не создана возникает ошибка
    from .menu import show_menu
    show_menu()
