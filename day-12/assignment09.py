class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        return (f"Processing payment")

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):
        return (f"Processed ${self.amount} by credit card")

class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):
        return (f"Processed ${self.amount} by Paypal")


payments = [
    CreditCardPayment(100, "1234"),
    PayPalPayment(75, "alex@example.com")
]

for payment in payments:
    print(payment.process())
