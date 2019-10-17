import re

txt = "The rain in Spain"
x = re.findall("ai", txt)  # Return a list containing every occurrence of "ai"
y = re.findall("portugal", txt)  # Check if "Portugal" is in the string
m = re.search("\s", txt)
n = re.search("portugal", txt)  # If no matches are found, the value None is returned
w = re.split("\s", txt) # Split at each white-space character
print(x)
print(y)
print("The first white-space character is located in position:", m.start())
print(n)
print(w)
