def takahasi(n , m , a):

    ans = "IMPOSSIBLE"
    list1n = []

    for i in range(m):
        if a[i][0] == 1 or a[i][1] == n:
            list1n.append(a[i][1] if a[i][0] == 1 else a[i][0])

    if len(list1n) != len(set(list1n)):
        ans = "POSSIBLE"

    return ans

def main():
    n , m = map(int , input().split())
    a = [list(map(int,input().split())) for i in range(m)]
    print(takahasi(n , m , a))

if __name__ == '__main__':
    main()