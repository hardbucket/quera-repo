# مجید و ماژیک‌هاش
n = int(input())
arr = list(map(int, input().split()))

counter = [0 for _ in range(max(arr)+ 1)]
arr_sorted = sorted(arr)

i = 0
while i < len(arr_sorted):
	if i == len(arr_sorted) - 1:
		counter[arr_sorted[i]] += 1
		break
	c = arr_sorted.count(arr_sorted[i])
	counter[arr_sorted[i]] += c
	i += c

filtered_counter = [x for x in counter if x != 0]
if n ==1:
    print(*arr)
else:
    print(counter.index(min(filtered_counter)))