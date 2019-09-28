a, b = map(int, input().split())
num = (b-a)//(a-1)
print (num+1 if (b-a)%(a-1) == 0 else num+2)
