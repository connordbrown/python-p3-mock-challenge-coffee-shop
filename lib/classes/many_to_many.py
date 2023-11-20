class Coffee:
    
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            raise Exception
        if not isinstance(name, str):
            raise Exception
        if not len(name) >= 3:
            raise Exception
        self._name = name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set(order.customer for order in Order.all if order.coffee == self))
    
    def num_orders(self):
        if self.orders():
            return len(self.orders())
        else:
            return 0
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        if prices:
            return sum(prices) / len(prices)
        else:
            return 0

class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception
        if not (1 <= len(name) <= 15):
            raise Exception
        self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set(order.coffee for order in Order.all if order.customer == self))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        customer_tabs = {}
        for customer in cls.all:
            customer_tabs[customer] = sum([order.price for order in coffee.orders() if order.customer == customer])
        highest = max(customer_tabs.values())
        top_customers = [cust for cust, sum in customer_tabs.items() if sum == highest]
        return top_customers[0] if top_customers else None

class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self, 'price'):
            raise Exception
        if not isinstance(price, float):
            raise Exception
        if not (1.0 <= price <= 10):
            raise Exception
        self._price = price