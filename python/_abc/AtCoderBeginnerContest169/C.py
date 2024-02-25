import math
import decimal
def c169(a, b):

    return math.floor(a*b)

def main():
    a, b = map(decimal.Decimal, input().split())
    print(c169(a, b))

if __name__ == '__main__':
    main()