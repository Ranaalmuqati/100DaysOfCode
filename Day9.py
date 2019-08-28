age = 23
name = "My Name is Rana, and I am {}."
print(name.format(age))
quantity = 3
item = 567
price = 49.95
My_order = "I want {} pieces of item {} for {} dollars. "
print(My_order.format(quantity, item, price))
My_order = "I want to pay {2} dollars for {0} pieces of item {1}. "
print(My_order.format(quantity, item, price))


