# مرتب کن!

def do_sort(alist):
    for r in range(1, n):
        for j in range(n - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


n, k = map(int, input().split())
a = list(map(int, input().split()))
arr = do_sort(a)
flag = False
ans = float("inf")
maxi =float("inf")
mini = 0

for i in range(len(arr) - 1):
    cnt = 1
    p = i + 1
    mini = max(mini, arr[p - 1])
    while p < n:

        if arr[p] != arr[p - 1]:

            cnt += 1
            if cnt == k:
                maxi = arr[p]
                ans = min(ans, maxi - mini)
                flag = True
        p = p + 1

if k == 1:
    flag = True
    ans = 0
if flag:
    print(ans)
if not flag:
    print(-1)
    