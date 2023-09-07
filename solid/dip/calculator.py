from abc import ABCMeta, abstractmethod


class Printer(metaclass=ABCMeta):
    @abstractmethod
    def print(self, add, multiply):
        pass


class Calculator:
    def __init__(self, a: int, b: int, printer: Printer) -> None:
        self.a = a
        self.b = b
        self.printer = printer

    def print(self) -> None:
        add = self.a + self.b
        multiply = self.a * self.b
        self.printer.print(add, multiply)
