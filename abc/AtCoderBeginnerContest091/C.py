
def Plane_2N(n, abli, cdli):

    ans = 0
    count = [0]*n

    abli.sort(key=lambda x: - x[1])
    cdli.sort()

    for i in cdli:
        for w in range(n):
            if abli[w][0] < i[0] and abli[w][1] < i[1] and count[w] == 0:
                ans += 1
                count[w] = 1
                break

    return ans

def main():
    n = int(input())
    abli = [list(map(int, input().split())) for i in range(n)]
    cdli = [list(map(int , input().split())) for i in range(n)]
    print(Plane_2N(n , abli , cdli))

if __name__ == '__main__':
    main()