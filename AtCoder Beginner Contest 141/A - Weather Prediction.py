# https://atcoder.jp/contests/abc141/tasks/abc141_a

arr = ['Sunny','Cloudy','Rainy']
a = input()
idx = 0
for i in range(len(arr)):
    if a in arr[i]:
        idx = i+1
print (arr[idx] if idx <= 2 else arr[idx % 3])
