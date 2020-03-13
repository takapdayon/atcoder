import math

def pushpush(n , a):

    ans = [a[i] for i in range(0 , n , 2)]
    ansb = [a[i] for i in range(1 , n , 2)]

    if n % 2 == 0:
        return ansb[::-1] + ans
    else:
        return ans[::-1] + ansb[::-1]

def main():
    n = int(input())
    a = list(map(int , input().split()))
    print(*pushpush(n , a))

if __name__ == '__main__':
    main()