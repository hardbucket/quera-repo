# مجید، میلاد، رشته‌سازی
L, R = map(int, input().split())

# create the string
st = "1"
while len(st) < R:
    for i in range(len(st)):
        
        if st[i] == "1":
            temp = "0"
            st += temp
            
        if st[i] == "0":
            temp = "1"
            st += temp

# slice from index L to R
print(st[L-1:R])