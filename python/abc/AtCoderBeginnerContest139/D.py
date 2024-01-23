def Alchemist(n , vl):

    vl.sort()
    ans = vl[0]

    for i in range(1 , n):
        ans = (ans + vl[i]) / 2

    return ans

def main():
    n = int(input())
    vl = list(map(int , input().split()))
    print(Alchemist(n , vl))

if __name__ == '__main__':
    main()