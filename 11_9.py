# جست‌وجوی دودویی

def binary_search(l, r, x):
    if r - l == 1:
        if arr[l] == x:
            return 1
        else:
            return 0
    mid = (r + l) // 2
    if x < arr[mid]:
        return binary_search(l, mid, x)
    else:
        return binary_search(mid, r, x)


n, q = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(q):
    num = input().split()[1]
    num = int(num)
    binary_search(0, len(arr), num )
    print(binary_search(0, len(arr), num))