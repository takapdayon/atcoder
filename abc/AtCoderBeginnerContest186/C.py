def c186(n):

    ans = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in str(oct(i)):
            ans += 1

    return ans

n = int(input())
print(c186(n))
