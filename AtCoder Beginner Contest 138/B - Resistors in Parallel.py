n = int(input())
a = list(map(int, input().split()))

den = 0
for i in range(n):
    den += 1/a[i]
print (1/den)
