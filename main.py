number = int(input("Enter a number: "))
digits = 0

while number > 0:
    number = number // 10
    digits = digits + 1

print("The number has", digits, "digits")
