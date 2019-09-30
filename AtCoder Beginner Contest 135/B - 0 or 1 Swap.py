n = int(input())
p = list(map(int, input().split()))
sorted_p = sorted(p)

cnt = 0
for i in range(n):
    if p[i] != i+1:
        cnt += 1
print ("NO" if cnt > 2 else "YES")
