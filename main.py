number = int(input("Enter a number: "))
digits = 0

while number > 0:
    number = number // 10
    digits += 1

print(f"The number has {digits} digits")
