def Chocolate(n , d , x , al):

    ans = n + x

    for i in range(n):
        ans += (d - 1) // al[i]

    return ans

def main():
    n = int(input())
    d, x = map(int, input().split())
    al = [int(input()) for i in range(n)]
    print(Chocolate(n , d , x , al))


if __name__ == '__main__':
    main()