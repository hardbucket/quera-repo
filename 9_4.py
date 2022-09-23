# گردو شکستم
dis, x, y = map(int, input().split())

# sort x = arz = min , y = tool = max
Reversed = False
if x > y:
    x, y = y, x
    Reversed = True
    
q = dis // x
rem = dis % x
new_dis = dis
reach = False
xsteps = 0
ysteps = 0
while rem <= dis:
    if rem % x == 0:
        xsteps = q + (rem // x)
        
        reach = True
        break
    elif rem % y == 0:
        ysteps = rem // y
        xsteps = new_dis // x
        reach = True
        break
    else:
        rem += x
        new_dis -= x

if reach:
    if Reversed:
        print(ysteps, xsteps)
    else:
        print(xsteps, ysteps)
if not reach:
    print(-1)
