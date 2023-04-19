from abc import ABC, abstractmethod
from typing import List
import os


class StateMachineInterface(ABC):
    def __init__(self, initial_state: "StateInterface") -> None:
        self.current_state = initial_state

    @abstractmethod
    def run(self) -> None:
        ...


class StateInterface(ABC):
    def __init__(self, title: str, states: List["StateInterface"]) -> None:
        self.title = title
        self.states = states

    @abstractmethod
    def draw(self, state_machine: StateMachineInterface) -> None:
        ...


class Menu(StateMachineInterface):
    def run(self) -> None:
        while True:
            self.current_state.draw(self)


class SelectorState(StateInterface):
    def draw(self, state_machine: StateMachineInterface) -> None:
        os.system("cls" if os.name == "nt" else "clear")

        print(f"====={self.title}=====\n")
        for serial_number, state in enumerate(self.states, 1):
            print(f"{serial_number}. {state.title}")
        print()

        try:
            user_choice = int(input("Введите номер пункта меню для выбора: "))
        except ValueError:
            print("Вы ввели недопустимое значение, попробуйте еще раз.\n")
            input("Нажмите ввод для продолжения")
            return

        if not 0 <= user_choice <= len(self.states):
            print("Пункта под данным номером нет в меню, попробуйте еще раз.\n")
            input("Нажмите ввод для продолжения")
            return

        state_machine.current_state = self.states[user_choice - 1]


def test():
    Menu(SelectorState(
        "Главное меню",
        [
            SelectorState("Ввести адрес", []),
            SelectorState("Настройки", []),
        ]
    )).run()


if __name__ == "__main__":
    test()