# اسنپ در شکرستان
r, c = map(int, input().split())

# To store value input in matrix
cost_matrix = []
for i in range(r):
    a = []
    cost = list(map(int, input().split()))
    for j in range(r):
        a.append(cost[j])
    cost_matrix.append(a)

# to store movement list splited into xlist and ylist
xlist = []
ylist = []
for i in range(c):
    destination_list = [int(x) for x in input().split()]
    xlist.append(destination_list[0]-1)
    ylist.append(destination_list[1]-1)

sum = 0
for i in range(c):
    travel_cost = cost_matrix[xlist[i]][ylist[i]]
    sum += travel_cost
print(sum)