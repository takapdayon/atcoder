def Traveling(n , txyl):

    ans = "No"
    count = 0
    for i in range(n):
        if txyl[i][0] >= txyl[i][1] + txyl[i][2] and txyl[i][0] % 2 == (txyl[i][1] + txyl[i][2]) % 2:
            count += 1

    if count == n:
        ans = "Yes"

    return ans

def main():
    n = int(input())
    txyl = [list(map(int , input().split())) for i in range(n)]
    print(Traveling(n , txyl))
    print(ans)

if __name__ == '__main__':
    main()
