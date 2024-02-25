import copy

def CakesandDonuts(n):

    ans = "No"
    a = copy.copy(n)

    if n % 7 == 0 or n % 4 == 0:
        ans = "Yes"
    else:
        while a > 0:
            n -= 7
            a -= 4
            if (n > 0 and n % 4 == 0) or (a > 0 and a % 7 == 0):
                ans = "Yes"

    return ans

def main():
    n = int(input())
    print(CakesandDonuts(n))

if __name__ == '__main__':
    main()