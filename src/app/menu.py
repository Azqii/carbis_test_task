from abc import ABC, abstractmethod
from typing import List, Optional, Callable

from .utils import clear, pause


class AbstractStateMachine(ABC):
    """Абстрактная State Machine"""

    def __init__(self, initial_state: "AbstractMenuState") -> None:
        self.current_state = initial_state

    @abstractmethod
    def run(self) -> None:
        ...


class AbstractMenuState(ABC):
    """Абстрактное состояние меню"""

    def __init__(self, title: str) -> None:
        self._title = title
        self.back_state: Optional["AbstractMenuState"] = None

    @abstractmethod
    def render(self, state_machine: AbstractStateMachine) -> None:
        ...


class Menu(AbstractStateMachine):
    """State Machine меню"""

    def run(self) -> None:
        while self.current_state:
            clear()
            self.current_state.render(self)


class SelectorState(AbstractMenuState):
    """Состояние из которого происходит выбор следующего состояния State Machine'ы"""

    def __init__(self, title: str, states: List["AbstractMenuState"]):
        super().__init__(title)
        self._states = states

    def render(self, state_machine: AbstractStateMachine) -> None:
        print(f"====={self._title}=====\n")
        for serial_number, state in enumerate(self._states, 1):
            print(f"{serial_number}. {state._title}")
        print("\n0.", "Назад\n" if self.back_state else "Выход\n")

        try:
            user_choice = int(input("Введите номер пункта меню для выбора: "))
        except ValueError:
            print("Вы ввели недопустимое значение, попробуйте еще раз.\n")
            pause()
            return

        if not 0 <= user_choice <= len(self._states):
            print("Пункта под данным номером нет в меню, попробуйте еще раз.\n")
            pause()
            return

        if user_choice == 0:
            state_machine.current_state = self.back_state
        else:
            state_machine.current_state = self._states[user_choice - 1]
            state_machine.current_state.back_state = self


class FunctionState(AbstractMenuState):
    """Состояние State Machine'ы из которого происходит вызов переданной функции"""

    def __init__(self, title: str, function: Callable[[AbstractMenuState, AbstractStateMachine], None]):
        super().__init__(title)
        self._function = function

    def render(self, state_machine: AbstractStateMachine) -> None:
        self._function(self, state_machine)


def find_coordinates(called_from_state: AbstractMenuState, state_machine: AbstractStateMachine) -> None:
    """Поиск координат"""
    print("Координаты найдены")  # FIXME: сделать нормальный поиск координат
    pause()
    state_machine.current_state = called_from_state.back_state


def show_settings(called_from_state: AbstractMenuState, state_machine: AbstractStateMachine) -> None:
    """Отображение настроек"""
    print("Настройки показаны")  # FIXME: сделать нормальное отображение настроек
    pause()
    state_machine.current_state = called_from_state.back_state


def set_russian_language(called_from_state: AbstractMenuState, state_machine: AbstractStateMachine) -> None:
    """Установка русского языка в настройках"""
    print("Язык изменен на русский")  # FIXME: сделать нормальную смену языка
    pause()
    state_machine.current_state = called_from_state.back_state.back_state


def set_english_language(called_from_state: AbstractMenuState, state_machine: AbstractStateMachine) -> None:
    """Установка английского языка в настройках"""
    print("Язык изменен на английский")  # FIXME: сделать нормальную смену языка
    pause()
    state_machine.current_state = called_from_state.back_state.back_state


def set_api_key(called_from_state: AbstractMenuState, state_machine: AbstractStateMachine) -> None:
    """Установка API-Ключа в настройках"""
    print("API-Ключ изменен")  # FIXME: сделать нормальную смену API-ключа
    pause()
    state_machine.current_state = called_from_state.back_state


def test():
    set_russian = FunctionState("Русский", set_russian_language)
    set_english = FunctionState("English", set_english_language)

    show_settings_menu = FunctionState("Показать настройки", show_settings)
    key_settings_menu = FunctionState("Изменить API-Ключ", set_api_key)
    language_settings_menu = SelectorState("Изменить язык возвращаемых ответов", [
        set_russian,
        set_english
    ])

    address_input = FunctionState("Поиск координат", find_coordinates)
    settings_menu = SelectorState("Настройки", [
        show_settings_menu,
        key_settings_menu,
        language_settings_menu,
    ])

    main_menu = SelectorState(
        "Главное меню",
        [
            address_input,
            settings_menu
        ])

    Menu(main_menu).run()


if __name__ == "__main__":
    test()
