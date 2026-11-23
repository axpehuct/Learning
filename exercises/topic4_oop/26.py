class Wallet:
    def __init__(self, owner, total = 0.0):
        self.owner = owner
        self._total = total

    def add(self, amount):
        self._total += amount

    def spend(self, amount):
        if amount > self._total:
            return False
        self._total -= amount
        return True

    def __str__(self):
        return f"Баланс {self._total}"

    def __eq__(self, value):
        return self.owner == value.owner and self._total == value.total
            
    
    @property
    def total(self):
        return self._total

wallet = Wallet("Igor")
wallet.spend(300)
wallet.add(500)
wallet.total = 5