# اندویست
q = int(input())

arr = [0 for _ in range(201)]

for i in range(q):
    row = input().split()
    order = row[0]
    color_num = int(row[1])
    if order == "+":
       arr[color_num] += color_num
    if order == "?":
        if arr[int(row[1])] == 0:
            print(0)
        else:
            print(int(arr[color_num] / color_num))