class Item:
  def __init__(self,name,price,quantity=0):
    self.name = name
    self.price = price
    self.quantity  = quantity

  def calculate_total_price(self):
    return self.price * self.quantity

item1 = Item("Phone",100,5)
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price,item1.quantity))
print(item1.calculate_total_price())

item2 = Item("Laptop",2000)
# item2.price = 300
# item2.quantity = 2
# print(item2.calculate_total_price(item2.price,item2.quantity))
print(item2.calculate_total_price())
