def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

def d180(x, y, a, b):

    ans = 0

    while a*x <= x+b and a*x < y:
        x *= a
        ans += 1

    return ans, x

x, y, a, b = map(int, input().split())
ans, retx = d180(x, y, a, b)
print(ans+(y-1-retx)//b)