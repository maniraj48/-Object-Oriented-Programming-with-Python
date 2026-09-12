from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Item("MyItem",750)

# setting an attribute
# item1.name = "OtherItem"

# item1.__price = 900

# getting an attribute
print(item1.name)
print(item1.price)

# item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)


item1.send_email()


item2 = Phone("Vivo",50000,2)
item2.apply_increment(0.2)

print(item2.price)
item2.send_email()


item3 = Keyboard("Mykey",750,2)
item3.apply_discount()
print(item3.price)