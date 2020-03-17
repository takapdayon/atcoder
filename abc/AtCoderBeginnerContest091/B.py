def Two_Colors(n , sl , m , tl):

    ans = 0
    count = {}

    for i in range(n):
        if sl[i] in count:
            count[sl[i]] += 1
        else:
            count[sl[i]] = 1

    for i in range(m):
        if tl[i] in count:
            count[tl[i]] -= 1
        else:
            count[tl[i]] = -1

    for i in count.values():
        ans = max(ans , i)

    return ans

def main():
    n = int(input())
    sl = [str(input()) for i in range(n)]
    m = int(input())
    tl = [str(input()) for i in range(m)]
    print(Two_Colors(n , sl , m , tl))


if __name__ == '__main__':
    main()