import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)  # Replace every white-space character with the number 9
y = re.sub("\s", "9", txt, 2)  # Replace the first two occurrences of a white-space character with the digit 9
z = re.search("ai", txt)  # The search() function returns a Match object
# Search for an upper case "S" character in the beginning of a word, and print its position
n = re.search(r"\bS\w+", txt)
print(x)
print(y)
print(z)
print(n.span())
print(n.group())  # Search for an upper case "S" character in the beginning of a word, and print the word
