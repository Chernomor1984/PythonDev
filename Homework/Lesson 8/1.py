from enum import Enum
import itertools

class Base:
    def __str__(self):
        return ""
    
    def __repr__(self):
        cls = type(self)
        return f"{cls}:\n{self.__str__()}"
    
class Product(Base):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price = value
    
    def __str__(self):
        return f"Product {self.__name}, it's price is {self.__price} $"
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented
        
class Customer(Base):
    def __init__(self, name):
        self.__name = name
        self.__orders = []
        
    @property
    def orders(self):
        return self.__orders
    
    def addOrder(self, order):
        self.__orders.append(order)
        
    def removeOrder(self, order):
        if order in self.__orders:
            self.__orders.remove(order)
            
    def __str__(self):
        ordersRepresentation = ""
        
        for index, order in enumerate(self.__orders, start=1):
            ordersRepresentation += f"\nOrder {index}:\n"
            ordersRepresentation += str(order)
            
        return f"Customer's name is {self.__name}, orders:{ordersRepresentation}"
        
class Order(Base):
    def __init__(self):
        self.__products = []
        
    @property
    def products(self):
        return self.__products
    
    def addProduct(self, product: Product):
        self.__products.append(product)
        
    def removeProduct(self, product: Product):
        if product in self.__products:
            self.__products.remove(product)
            
    @classmethod
    def flatten(cls, collection):
        return list(itertools.chain.from_iterable(collection))
            
    @classmethod
    def totalNumberOfOrders(cls, customers):
        return len(cls.flatten(list(map(lambda customer: customer.orders, customers))))
        
    @classmethod
    def totalCost(cls, customers):
        totalOrders = cls.flatten(list(map(lambda customer: customer.orders, customers)))
        totalProducts = cls.flatten(list(map(lambda order: order.products, totalOrders)))
        return sum(list(map(lambda product: product.price, totalProducts)))
    
    def __str__(self):
        productsRepresentation = "\n".join(list(map(lambda product: str(product), self.__products)))
        return f"{productsRepresentation}"

class DiscountType(Enum):
        season = 15
        promo = 20

class Discount(Base):
    def __init__(self, description, discount_percent):
        self.__description = description
        self.__discount_percent = discount_percent
        
    @property
    def description(self):
        return self.__description
    
    @property
    def discount_percent(self):
        return self.discount_percent
    
    @discount_percent.setter
    def discount_percent(self, value):
        self.__discount_percent = value
        
    @staticmethod
    def applyDiscount(order: Order, discount_percent: int | float):
        for product in order.products:
            product.price *= (1 - discount_percent / 100)
            
ford = Product("Ford", 1000)
bmw = Product("BMW", 2000)
honda = Product("Honda", 1500)
iPadMini = Product("iPad mini", 100)
iPadPro = Product("iPad Pro", 150)
iPhone17 = Product("iPhone 17", 120)
macBookPro = Product("MacBook Pro", 800)
macBookAir = Product("MacBook Air", 400)
john = Customer("John")
dick = Customer("Dick")
bill = Customer("Bill")

order1 = Order()
order1.addProduct(ford)
order2 = Order()
order2.addProduct(iPadMini)
order2.addProduct(macBookAir)
Discount.applyDiscount(order2, DiscountType.promo.value)
john.addOrder(order1)
john.addOrder(order2)

order3 = Order()
order3.addProduct(bmw)
order4 = Order()
order4.addProduct(iPadPro)
Discount.applyDiscount(order3, DiscountType.season.value)
dick.addOrder(order3)
dick.addOrder(order4)

order5 = Order()
order5.addProduct(honda)
order6 = Order()
order6.addProduct(iPhone17)
Discount.applyDiscount(order6, DiscountType.promo.value)
order7 = Order()
order7.addProduct(macBookPro)
bill.addOrder(order5)
bill.addOrder(order6)
bill.addOrder(order7)

customers = [john, dick, bill]
totalNumberOfOrders = Order.totalNumberOfOrders(customers)
totalCost = Order.totalCost(customers)

print(f"totalNumberOfOrders: {totalNumberOfOrders}, totalCost: {totalCost} $")
print()
print(*customers, sep="\n\n")