def ballrobot(n , k , xl):

    ans = 0

    for i in xl:
        if k - i < i:
            ans += k - i
        else:
            ans += i

    return ans*2

def main():
    n = int(input())
    k = int(input())
    xl = list(map(int , input().split()))
    print(ballrobot(n , k , xl))

if __name__ == '__main__':
    main()