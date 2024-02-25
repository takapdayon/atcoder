import math
def ccc(a, b):

    aaa = a * 12 + (a / 2)
    bbb = b * 10

    aan = math.floor(aaa * 0.1)
    ban = math.floor(bbb * 0.08)
    if b == bbb:
        return int(aaa)
    else:
        return "-1"

def main():
    a , b = map(int , input().split())
    print(ccc(a , b))

if __name__ == '__main__':
    main()