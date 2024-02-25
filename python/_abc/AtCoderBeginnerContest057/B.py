def ac(n,m,a,c):
    ans = []
    for i in range(n):
        min = 10000000000000
        bang = 0
        for w in range(m):
            if abs(a[i][0] - c[w][0]) + abs(a[i][1] - c[w][1]) < min:
                min = abs(a[i][0] - c[w][0]) + abs(a[i][1] - c[w][1])
                bang = w + 1
        ans.append(bang)
    return ans

def main():
    n , m = map(int, input().split())
    a = [list(map(int , input().split())) for i in range(n)]
    c = [list(map(int , input().split())) for i in range(m)]
    ans = ac(n , m , a , c)
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()
