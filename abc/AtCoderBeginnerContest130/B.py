def bounding(n, x, lli):

    ans = 1
    count = 0

    for i in lli:
        count += i
        if count <= x:
            ans += 1

    return ans
def main():
    n, x = map(int, input().split())
    lli = list(map(int, input().split()))
    print(bounding(n, x, lli))

if __name__ == '__main__':
    main()