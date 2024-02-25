import numpy as np
def Palace(n , t , a , hli):

    ans = 0
    count = 10**8

    for i in range(n):
        if abs(a - (t - hli[i] * 0.006)) < count:
            ans = i + 1
            count = abs(a - (t - hli[i] * 0.006))

    return ans

def main():
    n = int(input())
    t , a = map(int , input().split())
    hli = list(map(int , input().split()))
    print(Palace(n , t , a , hli))

if __name__ == '__main__':
    main()
