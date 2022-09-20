# اسم‌ها
n = int(input())

lst = [[],[]]
for _ in range(n):
    word = input()
    i = 0
    while i < len(word)  :
        j = i + 1
        while j < len(word):
            if word[i] == word[j]:
                word = word[:j] + word[j + 1:]
                continue
            j += 1
        i += 1

    lst[0].append(word)
    lst[1].append(len(word))

print(max(lst[1]))