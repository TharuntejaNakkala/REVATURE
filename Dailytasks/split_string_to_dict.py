#Split a structured string using a delimiter and map the parts to keys in a dictionary.
s = "Robert000Smith000123"
s1 = list(s.split('000'))
s2 = ['firstname', 'lastname', 'id']
print(dict(zip(s2, s1)))
