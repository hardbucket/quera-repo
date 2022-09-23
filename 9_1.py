# رشته تو رشته
s = input()
p = input()

lis = []
for i in range(len(s)):
    flag = "True"
    for j in range(len(p)):
        if 0 <= (i + j) < len(s):

            if s[i + j] != p[j]:
                flag = "False"
                continue
            # if s[i + j] == p[j]:
            #     flag = "True"
        else:
            flag = "False"
    if flag == "True":
        lis.append(i + 1)
        # print(i + 1 , end= " ")

print(*lis)