n,k,q = map(int, input().split())
a = n*[k]
for i in range(q):
    num = int(input())
    a[num-1] += 1
a = [k-q for k in a]
for i in range(n):
    if a[i] > 0:
        print ("Yes")
    else:
        print ("No")
