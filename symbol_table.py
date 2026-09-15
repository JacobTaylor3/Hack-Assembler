class SymbolTable:

    def __init__(self):

        self.table = {}

    def add_entry(self, symbol, address) -> None:
        self.table[symbol] = address

    def contains(self, symbol) -> bool:
        return symbol in self.table

    def get_address(self, symbol) -> str | None:
        return self.table.get(symbol)
