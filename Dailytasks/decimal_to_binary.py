#Convert a given number to its binary form.
n = int(input("Enter a number: "))
b = ""
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(f"Binary: {b}")
# Output: The binary representation of the input number.