import csv

class Item:
    pay_rate = 0.8 # price after 20% discount

    all = []

    def __init__(self,name: str,price: float,quantity=0):
        ## Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        ## Assign to self object
        self.__name = name
        self.__price = price
        self.quantity  = quantity

        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        # print("Your trying to get the name")
        return self.__name

    @property
    def price(self):
        return self.__price
    
    @name.setter
    def name(self,value):
        # print("Your setting an attribute")
        if len(value) > 10:
            raise Exception("The name is too long !")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price * increment_value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price = float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    def is_integer(num):
        # we will count out the floats that are point zero
        # For i.e : 5.0, 10.0
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    # @property
    # def read_only_name(self):
    #     return "AA"

# item1 = Item("Phone",100,5)
# item2 = Item("Laptop",2000,2)
# item3 = Item("Cable",10,5)
# item4 = Item("Mouse",50,5)
# item5 = Item("Keyboard",75,5)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(item1.price)
# print(Item.pay_rate)
# print(Item.__dict__)
# print(item1.__dict__)
# print(item2.pay_rate)


# Item.instantiate_from_csv()
# print(Item.all)

# for i in Item.all:
#   print(i.name)

# print(Item.is_integer(3))