from collections import Counter
left = []
right = []
with open('1.txt','r') as f:
    for line in f:
        l,r = line.split()
        left.append((int(l)))
        right.append((int(r)))

cnt_r = Counter(right)
ans = 0
for l in left:
    ans+=l*cnt_r[l]
print(ans)