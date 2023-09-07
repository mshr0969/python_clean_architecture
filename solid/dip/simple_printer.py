from calculator import Printer


class SimplePrinter(Printer):
    def print(self, add: int, multiply: int) -> None:
        print(f"a+b:{add}")
        print(f"a*b:{multiply}")
