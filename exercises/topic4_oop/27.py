from dataclasses import dataclass
from datetime import date

@dataclass
class Transaction:
    date: date
    rtype: str
    category: str
    amount: float

    def __str__(self):
        value = -self.amount if self.rtype == "expense" else self.amount 
        return f"{self.date} {value:+.2f} {self.category}"


transactions = [Transaction(date(2026, 10, 15), "income", "зарплата", 1000),
                Transaction(date(2026, 10, 17), "expense", "еда", 300),
                Transaction(date(2026, 10, 19), "expense", "машина", 500),]
for transaction in transactions:
    print(transaction)

print(transactions[0] == transactions[1])