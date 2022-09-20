# جمع دو ارایه
r, c = map(int, input().split())

# To receive input
a, b = [], []
for i in range(r):
    nums_a = list(map(int, input().split()))
    for num in nums_a:
        a.append(num)
for i in range(r):
    nums_b = list(map(int, input().split()))
    for num in nums_b:
        b.append(num)
# print(a, b)

# To calculate the sum list
s = 0
for i in range(r):
    sum_list = []
    for j in range(c*r):
        s = a[j] + b[j]
        sum_list.append(s)

# To convert sum_list to matrix with slicing
while sum_list != []:
    matrix = []
    matrix.extend(sum_list[:c])
    sum_list = sum_list[c:]
    print(*matrix)