import mymodule
import datetime

print("Task one:")
mymodule.add(1, 8)
mymodule.sub(4, 2)
mymodule.multi(6, 6)
mymodule.dividing(8, 2)

print("Task Two:")
x = datetime.datetime.now()
print(x.strftime("%c"))

print("task Three:")

today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)

tomorrow = today + datetime.timedelta(days=1)

print('Yesterday : ', yesterday)
print('Tomorrow : ', tomorrow)
