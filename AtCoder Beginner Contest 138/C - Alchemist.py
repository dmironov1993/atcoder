n = int(input())
v = list(map(int, input().split()))

while len(v) != 1:
    min_1 = min(v)
    del v[v.index(min_1)]
    min_2 = min(v)
    del v[v.index(min_2)]
    v.append((min_1 + min_2)/2)
    
print (v[0])
