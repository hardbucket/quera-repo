# مرتب‌سازی خفن!
class_list = []

n = int(input())
for i in range(n):
    name_list = input().split()
    mark_list = [float(x) for x in input().split()]
    sport_list = input().split()
    avg = sum(mark_list[1:]) // (mark_list[0])

    class_list += [[name_list, mark_list, sport_list, [avg]]]

for i in range(1, n):
    for j in range(n - 1):
        if class_list[j][3] < class_list[j + 1][3]:
            class_list[j], class_list[j + 1] = class_list[j + 1], class_list[j]
        if class_list[j][3] == class_list[j + 1][3]:
            if int(class_list[j][2][0]) < int(class_list[j + 1][2][0]):
                class_list[j], class_list[j + 1] = class_list[j + 1], class_list[j]
            if int(class_list[j][2][0]) < int(class_list[j + 1][2][0]):
                pass

for i in range(len(class_list)):
    print(*class_list[i][0])