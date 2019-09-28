n = int(input())
a = list(map(int, input().split()))
t = []
for i in range(1,n+1):
    t.append((a[i-1],i))
t = sorted(t)
arr = []
for k in range(n):
    arr.append(t[k][1])
print(*arr)
