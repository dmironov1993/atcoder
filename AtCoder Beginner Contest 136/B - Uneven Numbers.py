n = int(input())
arr = [len(str(p)) for p in range(1,n+1)]
cnt = 0
for i in range(n):
    if arr[i] % 2 != 0:
        cnt += 1
print (cnt)
