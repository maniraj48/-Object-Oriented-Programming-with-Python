class Item:
  pay_rate = 0.8 # price after 20% discount

  all = []

  def __init__(self,name,price,quantity=0):
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
    return f"Item('{self.name}',{self.price},{self.quantity})"
  

item1 = Item("Phone",100,5)
item2 = Item("Laptop",2000,2)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50,5)
item5 = Item("Keyboard",75,5)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(item1.price)
# print(Item.pay_rate)
# print(Item.__dict__)
# print(item1.__dict__)
# print(item2.pay_rate)

# print(Item.all)

for i in Item.all:
  print(i.name)