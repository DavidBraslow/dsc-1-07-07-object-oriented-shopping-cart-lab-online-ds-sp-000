import statistics

class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.items = []
        self.employee_discount = emp_discount
        
    def add_item(self, name, price, quantity=1):
        for i in range(0, quantity):
            self.items.append((name,price))
            self.total += price
        return self.total
            
    def mean_item_price(self):
        return self.total/len(self.items)

    def median_item_price(self):
        price_list = []
        for name, price in self.items:
            price_list.append(price)
        return statistics.median(price_list)

    def apply_discount(self):
        if self.employee_discount:
            return self.total * (100 - self.employee_discount)/100
        else:
            return 'Sorry, there is no discount to apply to your cart :('

    def void_last_item(self):
        if len(self.items) == 0 :
            return 'There are no items in your cart!'
        else:
            last_item, last_price = self.items.pop()
            self.total -= last_price
            return self.total