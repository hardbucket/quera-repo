# مرتب‌سازی ساده 
n = int(input())
arr = list(map(int, input().split()))

# Selection sort
for i in range(n):
    min_index = i
    for j in range(i, n):
        if arr[min_index] < arr[j]:
            min_index = j
            
    arr[min_index], arr[i] = arr[i], arr[min_index]

print(*arr)