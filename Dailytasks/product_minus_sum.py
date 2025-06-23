#For a given number, find the product of digits minus sum of digits.
n = int(input("Enter number: "))
l1 = []
prd = 1

while n > 0:
    l1.append(n % 10)
    n = n // 10

for i in l1:
    prd *= i

res = prd - sum(l1)
print(res)
# Output: The result of the product of digits minus the sum of digits.