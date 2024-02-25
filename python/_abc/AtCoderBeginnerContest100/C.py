def sanbun2(n , al):

    ans = 0

    for i in al:
        while i % 2 == 0:
            ans += 1
            i /= 2

    return ans

def main():
    n = int(input())
    al = list(map(int , input().split()))
    print(sanbun2(n , al))

if __name__ == '__main__':
    main()