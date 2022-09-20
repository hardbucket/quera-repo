# تغییرات ارایوی

q = int(input())

arr = []
for i in range(q):
    row = input().split()
    order = row[0]
    index = int(row[1])
    if order == "+":
        arr.insert(index - 1, int(row[2]))
    if order == "-":
        arr.pop(index - 1)
    if arr == []:
        print("EMPTY")
        continue
    print(*arr)