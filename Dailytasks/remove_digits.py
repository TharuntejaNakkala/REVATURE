#Remove all digits from an alphanumeric string.
a = 'H1e2l3l4o5w6o7r8l9d'
res = ''
for i in a:
    if not i.isdigit():
        res += i
print(res)
