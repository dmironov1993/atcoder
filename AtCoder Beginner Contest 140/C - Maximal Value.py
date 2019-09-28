# https://atcoder.jp/contests/abc140/tasks/abc140_c

n = int(input())
b = [*map(int, input().split())]

a = []
a.append(b[0])
for i in range(1,n-1):
    a.append(min(b[i],b[i-1]))
a.append(b[-1])
print (sum(a))



"""
n = int(input())
b = [*map(int, input().split())]

sum_a = b[0] + b[-1]
for i in range(1,n-1):
    sum_a += min(b[i],b[i-1])
print (sum_a)

"""
