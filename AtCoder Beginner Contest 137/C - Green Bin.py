from math import factorial as fac


def binomial(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom

n = int(input())
arr = []
for i in range(n):
    arr.append("".join(sorted(input())))

dct = {}
for i in range(n):
    if arr[i] not in dct.keys(): 
        dct[arr[i]] = 1
    else:
        dct[arr[i]] += 1
        
cnt = 0
l = len(dct.keys())
dctlist = list(dct.keys())
for i in range(l):
    el = dctlist[i]
    if dct[el] > 1:
        cnt += binomial(dct[el],2)
print(cnt)
