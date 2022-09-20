# تست بینایی
n = int(input())
char = input()
given_char = input()

count = 0
for i in range(n):
    if char[i] != given_char[i]:
        count += 1
print(count)