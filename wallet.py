if __name__ == '__main__':
    class Currency:
        def __init__(self, unit, value):
            self.unit = unit
            self.value = value

        def __str__(self):
            return f"{self.value} {self.unit}"


    class Bill(Currency):
        def __init__(self, value):
            super().__init__("dollar", value)


    class Coin(Currency):
        def __init__(self, value):
            super().__init("cent", value)
            
    class Wallet:
        def __init__(self, amount):
            self.contents = []
            self.fill_wallet(amount)

        def fill_wallet(self, amount):
        # Define the available bills and coins in descending order
            bill_coin_values = [100, 50, 20, 10, 5, 1, 25, 10, 5, 1]
            bill_coin_names = [
                "100 dollar bill", "50 dollar bill", "20 dollar bill",
                "10 dollar bill", "5 dollar bill", "1 dollar bill",
                "25 cent coin", "10 cent coin", "5 cent coin", "1 cent coin"
                ]

            for value, name in zip(bill_coin_values, bill_coin_names):
                num_bills_coins, amount = divmod(amount, value)
                if num_bills_coins > 0:
                    self.contents.append((num_bills_coins, name))

        def display_wallet_contents(self):
            if not self.contents:
                print("Your wallet is empty.")
            else:
                for num_bills_coins, name in self.contents:
                    print(f"{num_bills_coins} {name}")
        
    amount = float(input("Enter the amount of money in your wallet: "))
    wallet = Wallet(amount)
    wallet.display_wallet_contents()