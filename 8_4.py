# چاپ برعکس
lst = []
while True:
    n = int(input())
    if n == 0:
        break
    else:    
        lst.append(n)
        continue


rev_lst = lst[::-1]
for i in rev_lst:
    print(i)