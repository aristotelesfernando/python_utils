n1 = input("Enter a number: ")
n2 = input("Enter another number: ")

dif = float(n1) - float(n2)

print(f"The difference between {n1} and {n2} is an integer? {dif.is_integer()}")
