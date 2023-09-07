## 依存性逆転の理解
a+bとa*bをCLI上かjsonで出力する例を通して依存性逆転を理解する。
#### ディレクトリ構成
```
.
├── README.md
├── calculator.py
├── csv_printer.py
├── json_printer.py
├── main.py
└── simple_printer.py
```

もし、calculator.pyの`Calculator`クラスの`print`メソッドで出力処理を書いた時に、
```
class Calculator():
    def __init__(self, a: int, b: int, mode: str) -> None:
        self.a = a
        self.b = b
        self.mode = mode

    def print(self) -> None:
        add = self.a + self.b
        multiply = self.a * self.b

        # 出力方法を切り替える
        if self.mode == 'json':
            json_printer = JsonPrinter()
            json_printer.print(add, multiply)
        elif self.mode == 'simple':
            simple_printer = SimplePrinter()
            simple_printer.print(add, multiply)
```
のようにしてしまうと、`Calculator`という"処理"が`Printer`という"出力"に依存してしまう
#### 依存しているとは
AがBに依存しているとは、Bの変更にAが影響されるということ

つまり、**出力を変えたいだけなのに処理も変えないといけない**という状況になっている。

例えば今後「csv形式で出力したい」という要望が来た時に、`Calculator`クラスまで変更する羽目になる！


### 依存性の逆転
これを解消するために、`Printer`という抽象クラスを作成し、`JsonPrinter`、`SimplePrinter`に継承させる。

すると、"出力"が"処理"に依存する(さっきは逆だった！)

`Calculator`クラスには、`Printer`を引数に入れることで、例えば`CsvPrinter`というクラスを追加しても影響されなくなる

→**依存性逆転**

`main.py`でmodeを変更するだけで出力先が変更できる
