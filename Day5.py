x = "apple"
y = "orange"
z = "lemon"
basket = x, y, z
n = 6
[basket[i:i+n] for i in range(0, len(basket), n)]
print(basket)







