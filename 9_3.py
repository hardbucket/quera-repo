#اوقات فراغت 
n, m = map(int, input().split())
a = []
for i in range(n):
    word = input()
    lst = []
    for x in word:
        lst.append(x)
    a.append(lst)

s = [str(x) for x in input()]

count = 0
for i in range(n):
    for j in range(m):
        diff = 0
        for k in range(0, len(s)):
            if k + j < m:
                if s[k] != a[i][k + j]:
                    diff = 1
        
        if k + j < m:    
            if diff == 0:
                count += 1
for i in range(n):
    for j in range(m):
        diff = 0
        for k in range(len(s)):
            if k + i < n:
                if s[k] != a[i + k][j]:
                    diff = 1
        if k + i < n:
            if diff == 0:
                count += 1
print(count)