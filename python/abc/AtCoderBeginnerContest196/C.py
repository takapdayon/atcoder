def c196(n):

    ans = 0
    keta = len(str(n)) // 2

    for i in range(keta):
        start = 10 ** i
        end = "9" * (i+1)
        while start <= int(end):
            atai = f"{start!s}{start!s}"
            if int(atai) > n:
                break
            ans += 1
            start += 1

    return ans

n = int(input())
print(c196(n))
