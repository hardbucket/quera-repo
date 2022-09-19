# باقر خسته‌ست ولی بی‌فرهنگ نه
n, l = map(int, input().split())

light_list = []
for light_num in range(n):
    light_instance = list(map(int, input().split()))
    light_list.append(light_instance)

overall_dis = 0
time = 0
for i in range(n):
    if i == 0:
        d = light_list[i][0]
        overall_dis += d
        time += d
        light_cycle = light_list[i][1] + light_list[i][2]
        if time % (light_cycle) < light_list[i][1]:
            time += (light_list[i][1] - (time % (light_cycle)))
    else:
        d = light_list[i][0] - light_list[i - 1][0]
        overall_dis += d
        time += d
        light_cycle = light_list[i][1] + light_list[i][2]
        if time % (light_cycle) < light_list[i][1]:
            time += (light_list[i][1] -(time % (light_cycle)))
time += (l - overall_dis)
print(time)