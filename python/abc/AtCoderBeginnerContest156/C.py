def rally(n , xl):

    ans = 0

    aaa = round(sum(xl) / n)

    for i in range(n):
        ans += (xl[i] - aaa)**2

    return ans

def main():
    n = int(input())
    xl = list(map(int , input().split()))
    print(rally(n , xl))

if __name__ == '__main__':
    main()
