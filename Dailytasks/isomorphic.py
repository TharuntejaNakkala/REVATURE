"""Check whether two strings are isomorphic. Two strings are isomorphic if characters in one string can be replaced to get the second string, maintaining the order and uniqueness of mappings."""
def is_isomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))


input_s = "egg"
input_t = "add"

output = is_isomorphic(input_s, input_t)
print("Are the strings isomorphic?", output)
