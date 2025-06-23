import math         
# Find permutation and combination for given n and r.   

def perm(n, r):
    return math.factorial(n) // math.factorial(n - r)

def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n = 9
r = 3
print(perm(n, r))
print(comb(n, r))
