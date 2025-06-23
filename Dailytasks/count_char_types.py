"""Count how many lowercase, uppercase, digits, and special characters are in a string."""
string = input("Enter a string: ")

l_count = 0
u_count = 0
d_count = 0
spl_count = 0

for i in string:
    if i.islower():
        l_count += 1
    elif i.isupper():
        u_count += 1
    elif i.isdigit():
        d_count += 1
    else:
        spl_count += 1

print("lower", l_count)
print("upper", u_count)
print("digit", d_count)
print("spcl", spl_count)
