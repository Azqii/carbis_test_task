import os


def clear() -> None:
    """Очищает консоль"""
    os.system("cls" if os.name == "nt" else "clear")


def pause() -> None:
    """Приостанавливает выполнение программы до нажатия клавиши Ввод"""
    input("(Нажмите Ввод для продолжения)")
