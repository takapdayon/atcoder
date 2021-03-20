def c195(n):
    if int(n) <= 999:
        return 0

    ans = 0
    count = len(n) // 3 if len(n)%3 != 0 else len(n) // 3 - 1
    revn = n[::-1]


    for i, mn in enumerate(revn):
        ans += ((10 **(i))*int(mn)) * count
        if (i+1) == len(n):
            ans -= int('100'*count)*10
    ans += count

    return ans

n = str(input())
print(c195(n))
