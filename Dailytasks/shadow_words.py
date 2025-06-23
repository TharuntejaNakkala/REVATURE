#Check if two phrases are "shadow words" — words at corresponding positions must have the same length and no common characters.
s = "his friends"
s1 = "our company"

def shadowword(s, s1):
    f1 = s.split(' ')
    f2 = s1.split(' ')
    if len(f1) != len(f2):
        return False
    for w1, w2 in zip(f1, f2):
        if (set(w1) & set(w2)):  # Check common characters
            return False
        if len(w1) != len(w2):  # Check equal length
            return False
    return True

print(shadowword(s, s1))
