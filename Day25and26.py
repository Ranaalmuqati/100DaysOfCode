# task one
print("Task One:")
set = {1, 3, 5, 7, 8}
set.update([4, 8, 12])
print(set)
set.remove(8)
print(set)
set.clear()
print(set)

# task two
print("Task Two:")
pigeon = {
  "name": "pigeon",
  "type": "bird",
  "skinCover": "feathers"
}
x = pigeon.get("type")
print(x)
pigeon["skinCover"] = "null"
print(pigeon)

