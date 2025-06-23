#Print symmetric difference of two sets (elements in either but not both).
n = int(input())
l1 = set(map(int, input().split()))
m = int(input())
l2 = set(map(int, input().split()))
res = l1 ^ l2
print(res)
