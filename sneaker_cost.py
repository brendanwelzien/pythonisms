class Sneaker:
    def __init__(self, name, retail_value=0, market_value=0):
        self.name = name
        self.retail_value = retail_value
        self.market_value = market_value
        self.profits = []
    
    def __str__(self):
        return f'{self.name} retail price is ${self.retail_value} while its market price is ${self.market_value}.'


    def add_profits(self, purchase_cost, sold_cost):
        if not isinstance(purchase_cost, int):
            raise ValueError('Enter a number amount')
        if not isinstance(sold_cost, int):
            raise ValueError('Enter a number amount')
        transaction = sold_cost - purchase_cost
        self.profits.append(transaction)
    
    @property
    def total_profits(self):
        return sum(self.profits)

    def __len__(self):
        return len(self.profits)

    def __getitem__(self, sale):
        return self.profits[sale]

jordanOne = Sneaker('Jordan One Shadow Grey', 170, 500)
jordanOne.add_profits(180, 500)
jordanOne.add_profits(250, 150)
jordanOne.add_profits(480, 0)
jordanOne.add_profits(230, 450)
print(jordanOne.total_profits)
print(len(jordanOne))
print(jordanOne.__getitem__[0])
