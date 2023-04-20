# import sys

# from app.utils import menu
# from app.db import create_db
from app.menu import test


def execute_from_cmd(argv) -> None:
    """Вызывает нужную функцию в зависимости от переданного аргумента"""
    # if argv[1] == "createdb":
    #     create_db()
    # elif argv[1] == "start":
    #     menu()


def main():
    # execute_from_cmd(sys.argv)
    test()


if __name__ == "__main__":
    main()
