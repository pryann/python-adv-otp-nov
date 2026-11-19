# array
import array as arr
from collections import Counter
from operator import inv

my_array = arr.array("i", [1, 2, 3, 4, 5])
print(my_array)
print(my_array.itemsize)
print(len(my_array))
print(my_array[1])
my_array.append(6)
print(my_array)
my_array.pop()
print(my_array)
print(sum(my_array))

# frozenset
companies = {"Anthropic", "Apple", "Microsoft", "Adobe"}
print(companies)
companies.add("Nvidia")
print(companies)

frozen_companies = frozenset(companies)
print(type(frozen_companies), frozen_companies)

# counter
inventory = Counter()
inventory.update({"xp": 12_000, "gold": 1113, "potion": 4})
print(inventory)
inventory.update({"xp": 1000, "gold": -100, "silver": 111})
print(inventory)
inventory.pop("gold")
print(inventory)
inventory.clear()
print(inventory)
