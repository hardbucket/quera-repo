# چالش شنگدباو 
q =int(input())
arr= []
for _ in range(q):
    order, order_num = input().split()
    order_num = int(order_num)
    
    if order == "Add":
        arr.append(order_num)
        arr.sort()
    elif order == "Ask":
        # new_arr = arr[:]
        print(arr[order_num - 1])