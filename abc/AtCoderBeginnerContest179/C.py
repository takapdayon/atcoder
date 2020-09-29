def c179(n):

    ans = 0

    for i in range(1, n):
        for w in range(1, n):
            if i * w < n:
                ans += 1
            else:
                break

    return ans

def main():
    n = int(input())
    print(c179(n))

if __name__ == '__main__':
    main()