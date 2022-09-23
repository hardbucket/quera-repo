# پُرّشته
def toString(List):
    num = ''.join(List)
    a_list.append(num)
    return a_list


def permute(a, l, r):
    if l == r:
        return toString(a)

    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


a_list = []
x = input()
n = len(x)
a = list(x)
permute(a, 0, n)

sorta = sorted(a_list)
# print(sorta)
for i in range(len(sorta)):
    if int(sorta[i]) > int(x):
        print(sorta[i])
        break
else:
    print(0)