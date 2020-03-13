def cityroadcount(n , m , a):
    reans = []
    for i in range(1 , n + 1):
        count = 0
        for w in range(m):
            count += int(a[w].count(i))
        reans.append(count)

    return reans

def main():
    n , m = map(int, input().split())
    a = [list(map(int,input().split())) for i in range(m)]

    ans = cityroadcount(n , m , a)
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()