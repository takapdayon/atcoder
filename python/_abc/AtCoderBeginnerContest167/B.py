def b167(a, b, c, k):

    ans = 0

    if k >= a:
        ans += a
        if (k-a) >= b:
            ans -= (k-a-b)
    else:
        ans = k
    return ans
def main():
    a, b, c, k = map(int, input().split())
    print(b167(a, b, c, k))

if __name__ == '__main__':
    main()