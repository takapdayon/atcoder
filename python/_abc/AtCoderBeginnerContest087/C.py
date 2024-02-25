def Candies(n , a1l , a2l):

    ans = 0

    for i in range(n):
        count = sum(a1l[:i + 1]) + sum(a2l[i:])
        ans = max(ans , count)
    return ans

def main():
    n = int(input())
    a1l = list(map(int , input().split()))
    a2l = list(map(int , input().split()))
    print(Candies(n , a1l , a2l))

if __name__ == '__main__':
    main()
