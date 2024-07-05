class SpecialSymbol:
    def __init__(self, symbols) -> None:
        self.symbols = symbols

    def findSpecialSymbol(self, symbol):
        if symbol in self.symbols:
            return True
        return False