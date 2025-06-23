#Reverse a given string character by character.
str = "rise to vote sir"
new = ""
for i in str[::-1]:
    new += i
print(new)
