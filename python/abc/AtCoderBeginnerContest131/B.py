def bite_eating(n, l):

    count = 0
    ans = 10**5
    ansmin = 0

    for i in range(1, n+1):
        if ans > abs(i+l-1):
            ans = abs(i+l-1)
            ansmin = i+l-1
        count += (i+l-1)

    return count - ansmin
def main():
    n, l = map(int, input().split())
    print(bite_eating(n, l))

if __name__ == '__main__':
    main()
