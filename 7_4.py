# قطار کامیابی
k , a , b = map(int, input().split())

# if they are at the same place
if a == b:
    print(0)

# find the lowest of a and b and set it to a
if a > b:
    a, b = b, a

# if the lowest is a then ok
if a < b:
    # if two metro are the same
    if k == 1:
        minutes = -a + b

    if b - a <= (k // 2):
        minutes = b - a

    if b - a > (k // 2):
        minutes = 0
        if (a % k) < (k / 2):
            minutes += (a % k)
            a -= (a % k)

            if (b % k) > (k / 2):
                minutes += (k - (b % k))
                b += (k - (b % k))
                minutes += (b - a) // k
            else:
                minutes += (b % k)
                b -= (b % k)
                minutes += (b - a) // k
        else:
            minutes += (k - (a % k))
            a += (k - (a % k))

            if (b % k) > (k / 2):
                minutes += (k - (b % k))
                b += (k - (b % k))
                minutes += (b - a) // k
            else:
                minutes += (b % k)
                b -= (b % k)
                minutes += (b - a) // k

    print(minutes)