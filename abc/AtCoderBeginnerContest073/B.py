def theater(n , lt):

    ans = 0

    for i in range(n):
        ans += (lt[i][1] - lt[i][0]) + 1

    return ans

def main():
    n = int(input())
    lt = [list(map(int , input().split())) for i in range(n)]
    print(theater(n , lt))

if __name__ == '__main__':
    main()