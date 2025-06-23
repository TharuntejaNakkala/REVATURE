#Split the English lowercase alphabet string into equal parts of size l.
str = "abcdefghijklmnopqrstuvwxyz"
l = 4
for i in range(0, len(str), l):
    print(str[i:i+l])
