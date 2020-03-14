def c(n , m , scl):

    ans = ""
    count = {}

    for i in range(m):
        if scl[i][0] in count:
            if count[scl[i][0]] > scl[i][1]:
                if scl[i][0] != 1 and scl[i][1] != 0:
                    count[scl[i][0]] = scl[i][1]
        elif scl[i][0] != 1 and scl[i][1] != 0:
            count[scl[i][0]] = scl[i][1]

    for i in range(1 , n + 1):
        if i not in count:
            count[i] = 0

    if count[1] == 0 and n != 1 or m == 0:
        return "-1"

    for i in range(1 , n + 1):
        ans += str(count[i])

    if len(ans) != n:
        return "-1"

    return ans

def main():
    n , m = map(int , input().split())
    scl = [list(map(int , input().split())) for i in range(m)]
    print(c(n , m , scl))

if __name__ == '__main__':
    main()
