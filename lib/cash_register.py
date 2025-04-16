class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = [] 
        self.discount = discount
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
        self.last_transaction_amount = price * quantity
        self.total += self.last_transaction_amount

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            if self.total.is_integer():
                print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
                print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        print("Last transaction voided.")
