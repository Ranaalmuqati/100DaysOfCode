import datetime
x = datetime.datetime.now()
print(x)
print(x.year)  # Return the year
print(x.strftime("%A"))  # Return the name of day

x = datetime.datetime(2020, 5, 17)
print(x)

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))  # Return the month




