import re

txt = "The rain in Spain 2"
x = re.search("^The.*Spain$", txt)
z = re.findall("\d", txt)  # #Find all digit characters
# Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character)
m = re.findall("\w", txt)
n = re.findall("[arn]", txt)  # Check if the string has any a, r, or n characters
s = re.findall("[0123]", txt) # Check if the string has any 0, 1, 2, or 3 digits
print(z)
print(m)
print(n)
print(s)
if (x):
    print("Yes! We have a match!")
else:
    print("No match")


string = "The rain in Spain falls mainly in the plain!"
y = re.findall("al{2}", string)  # Check if the string contains "a" followed by exactly two "l" characters:

print(y)
if (y):
    print("Yes! We have a match!")
else:
    print("No match")
