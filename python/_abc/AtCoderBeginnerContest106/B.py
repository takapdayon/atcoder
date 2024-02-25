def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return len(divisors)

def Yakusu(n):

    ans = 0

    for i in range(1 , n + 1 , 2):
        if make_divisors(i) == 8:
            ans += 1

    return ans

def main():
    n = int(input())
    print(Yakusu(n))

if __name__ == '__main__':
    main()