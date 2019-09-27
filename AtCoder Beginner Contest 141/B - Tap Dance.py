# https://atcoder.jp/contests/abc141/tasks/abc141_b

string = input()
odd = 'RUD'
even = 'LUD'
ans = "Yes"
for i in range(len(string)):
    if (i % 2 != 0 and string[i] not in even) or (i % 2 == 0 and string[i] not in odd):
        ans = "No"
        break
print (ans)
