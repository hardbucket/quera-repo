# سوال : جمع دو ارایه
n = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

lst_sum = []
for i in range(n):
    lst_sum.append(lst1[i] + lst2[i])
    
for j in lst_sum:
    print(j, end=" ")