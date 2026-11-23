fruit = ["банан", "киви", "арбуз", "Черешня", "айва"]
print(sorted(fruit, key = str.casefold))
print(sorted(fruit, key = lambda i: (len(i), i.lower())))