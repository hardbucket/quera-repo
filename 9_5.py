# جوس
s = input()  * 2
p = input()

if len(s) < (len(p) * 2) + 1:
    num_of_lens = (2 * len(p) // len(s)) + 1
    s = s * num_of_lens

if p in s:
    print("Yes")
if p not in s:
    print("No")