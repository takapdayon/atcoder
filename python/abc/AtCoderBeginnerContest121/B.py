def can_you_solve_this(n, m, c, bl, al):

    ans = 0

    for i in al:
        count = 0
        for w in range(len(bl)):
            count += bl[w]*i[w]
        if count+c > 0:
            ans += 1

    return ans

def main():
    n, m, c = map(int, input().split())
    bl = list(map(int, input().split()))
    al = [list(map(int, input().split()))for i in range(n)]
    print(can_you_solve_this(n, m, c, bl, al))

if __name__ == '__main__':
    main()
