n = int(input())
h = list(map(int, input().split()))

ans = 0
step = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        step += 1
    else:
        ans = max(ans, step)
        step = 0
print (max(ans, step))
