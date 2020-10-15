# decorator is a function which accepts a function, enhances it, and returns it

class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100
    
    @property
    def dollars(self):
        return f"${self._cents / 100:,.2f}"
    
bank_acct = Currency(50_000)
print(bank_acct.dollars)