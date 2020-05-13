from math import gcd
def anti_division(a, b, c, d):

    ans = b-a+1
    cd = a*b // gcd(a, b)
    ccount = ((b+c)//c) - ((a+c-1)//c)
    dcount = ((b+d)//d) - ((a+d-1)//d)
    cdcount = ((b+cd)//cd) - ((a+cd-1)//cd)

    return ans-ccount-dcount+cdcount
def main():
    a, b, c, d = map(int, input().split())
    print(anti_division(a, b, c, d))

if __name__ == '__main__':
    main()