def Sum(n):
    s = str(n)
    sli = list(map(int , s))

    return sum(sli)

def DigitSums(n):

    digitsum = Sum(n)

    return "Yes" if n % digitsum == 0 else "No"

def main():
    n = int(input())
    print(DigitSums(n))

if __name__ == '__main__':
    main()