import math
def c168(a, b, h, m):

    hh = h*30+0.5*m
    mm = 6*m

    kaku = abs(hh - mm) if 180 >= abs(hh - mm) else 360 - abs(hh - mm)

    ss = math.cos(kaku*math.pi/180)

    ans = math.sqrt((a**2 + b**2-2*a*b*ss))

    return ans

def main():
    a, b, h, m = map(int, input().split())
    print(c168(a, b, h, m))

if __name__ == '__main__':
    main()