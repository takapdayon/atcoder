from math import gcd

def snack(a, b):

    icm = (a*b // gcd(a, b))
    return icm

def main():
    a, b = map(int, input().split())
    print(snack(a, b))

if __name__ == '__main__':
    main()