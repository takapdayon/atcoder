def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

def c180(n):

    return make_divisors(n)

n = int(input())
ret = c180(n)
for i in ret:
    print(i)