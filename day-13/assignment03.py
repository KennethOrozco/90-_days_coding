from dataclasses import dataclass

@dataclass
class BankAccount:
    owner:str
    balance: float = 0.0
    
    def __post_init__(self) -> None:
        if self.balance < 0:
            raise ValueError("Balance cannot be negative")

    def deposit(self, amount:float) -> float:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance

account = BankAccount("Alex", 100.0)

print(account.deposit(50.0))
print(account)

