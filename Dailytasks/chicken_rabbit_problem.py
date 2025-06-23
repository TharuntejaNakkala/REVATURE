#Given total heads and legs, find number of chickens and rabbits.
heads = 35
legs = 94
for r in range(heads + 1):
    c = heads - r
    if 2 * c + 4 * r == legs:
        print(c, r)
        break
else:
    print(None)
