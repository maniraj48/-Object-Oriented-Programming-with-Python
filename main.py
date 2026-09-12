import csv
class Item:
  pay_rate = 0.8 # price after 20% discount

  all = []

  def __init__(self,name: str,price: float,quantity=0):
    ## Run validations to the received arguments
    assert price >= 0, f"Price {price} is not greater or equal to zero"
    assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

    ## Assign to self object
    self.name = name
    self.price = price
    self.quantity  = quantity

    Item.all.append(self)

  def calculate_total_price(self):
    return self.price * self.quantity

  def apply_discount(self):
    self.price = self.price * self.pay_rate

  def __repr__(self):
    return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

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

class Phone(Item):
  def __init__(self,name: str,price: float,quantity=0,broken_phones=0):
    # Call to super function to have access to all attributes / methods
    super().__init__(
      name,price,quantity
    )

    ## Run validations to the received arguments
    assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero"

    ## Assign to self object
    self.broken_phones = broken_phones


phone1 = Phone("Vivo",60000,3,0)
phone2 = Phone("Samsung",20000,2,1)

# print(phone1.calculate_total_price())
# print(phone2.calculate_total_price())

# print(Item.all)
print(Phone.all)
