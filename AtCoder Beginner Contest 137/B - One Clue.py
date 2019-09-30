k, x = map(int, input().split())
if k > 1:
    print (*([p for p in range(x-k+1,x+1)] + [p for p in range(x+1, x+k)]))
else:
    print (x)
