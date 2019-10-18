import json
import re

print("Task one:")
weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
print(json.dumps(weekdays))


print("Task Two:")
txt = "data is the new oil"
x = re.search("data", txt)
print(x)

