x = int(input())

s , a = divmod(x , 11)

if a > 6:
    print((s*2) + 2)
elif a == 0:
    print((s*2))
else:
    print((s*2) + 1)