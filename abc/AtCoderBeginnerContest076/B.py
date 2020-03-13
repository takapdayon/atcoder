def doubleork(n, k):

    ans = 1

    for i in range(n):
        if ans * 2 < ans + k:
            ans *= 2
        else:
            ans += k

    return ans


def main():
    n = int(input())
    k = int(input())
    print(doubleork(n , k))


if __name__ == '__main__':
    main()