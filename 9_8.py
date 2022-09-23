# پیدا کن!
n, q = map(int, input().split())
alist = list(map(int, input().split()))

for _ in range(q):
    x = int(input().split()[1])
    left = 0
    right = len(alist)
    while left < right:
        mid = (left + right) // 2
        if alist[mid] == x:
            left = right = mid
            break
        if x < alist[mid]:
            right = mid - 1
        if x > alist[mid]:
            left = mid + 1
    if alist[left] == x:
        print(1)
    else:
        print(0)
