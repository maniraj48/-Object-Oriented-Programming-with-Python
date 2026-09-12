from item import Item

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
