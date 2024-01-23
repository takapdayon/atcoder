def resale(n, vli, cli):

    ans = 0

    for i in range(len(vli)):
        if vli[i]-cli[i] > 0:
            ans += vli[i]-cli[i]

    return ans

def main():
    n = int(input())
    vli = list(map(int, input().split()))
    cli = list(map(int, input().split()))
    print(resale(n, vli, cli))

if __name__ == '__main__':
    main()