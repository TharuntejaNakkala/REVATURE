#Given two strings, where the second string contains all characters of the first plus one extra, find and return the extra character.
def rmv_extra(s, s1):
    for i in s1:
        if i not in s:
            return i

s = "eueiieo"
s1 = "iieoedue"
print(rmv_extra(s, s1))
