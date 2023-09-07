from calculator import Calculator, Printer
from simple_printer import SimplePrinter
from json_printer import JsonPrinter

if __name__ == "__main__":
    a = 2
    b = 4
    mode = "json"
    if mode == "json":
        printer: Printer = JsonPrinter()
    else:
        printer: Printer = SimplePrinter()
    calculator = Calculator(a, b, printer)
    calculator.print()
