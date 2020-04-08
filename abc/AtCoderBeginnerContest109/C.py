from fractions import gcd
from functools import reduce

def Skip(n , x , xl):

    xl = map(lambda i: abs(i - x), xl)
    return reduce(gcd , xl)

def main():
    n , x = map(int , input().split())
    xl = list(map(int , input().split()))
    print(Skip(n , x , xl))

if __name__ == '__main__':
    main()