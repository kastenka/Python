#
class VendingMachine:
    def __init__(self, num, price):
        self.num_items = num
        self.item_price = price

    """
    method buy(req_items, money) represents a buy request
    req_items denotes the requested number of items
    money is the amount the customer puts into the machine
    """
    def buy(self, req_items, money):
        if req_items <= self.num_items:  # if amount of items is OK
            if money < self.item_price * req_items:  # if given amount of money is less than cost of items
                raise ValueError("Not enough coins")
            else:
                self.num_items -= req_items  # subtract
                return money - req_items * self.item_price  # return the change given back after the purchase
        else:
            raise ValueError("Not enough items in the machine")


deal = VendingMachine(12, 3)
items1, items2 = 15, 10
money1, money2 = 10, 50

print(deal.buy(items1, money1))  # output: raise ValueError("Not enough items in the machine")
print(deal.buy(items2, money2))  # output: 20
print(deal.buy(items2, money1))  # output: raise ValueError("Not enough coins")



