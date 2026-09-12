from item import Item

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
# print(Phone.all)
