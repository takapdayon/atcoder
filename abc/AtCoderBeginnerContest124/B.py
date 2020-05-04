def great_ocean_view(n, hli):

    ans = 0
    hlimax = hli[0]

    for i in hli:
        if hlimax <= i:
            ans += 1
            hlimax = i

    return ans

def main():
    n = int(input())
    hli = list(map(int, input().split()))
    print(great_ocean_view(n, hli))

if __name__ == '__main__':
    main()