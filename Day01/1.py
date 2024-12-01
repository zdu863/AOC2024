left = []
right = []
with open('1.txt','r') as f:
    for line in f:
        l,r = line.split()
        left.append((int(l)))
        right.append((int(r)))
        
ans = 0
for l, r in zip(sorted(left), sorted(right)):
    ans += abs(l-r)
print(ans)