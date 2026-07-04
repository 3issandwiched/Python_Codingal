size = 5

for i in range(1, size + 1):
    spaces = " " * (size - i)
    stars = "*" * i
    print(spaces + stars)