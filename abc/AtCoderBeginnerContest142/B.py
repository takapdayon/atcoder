import bisect
def roller_coaster(n, k, hli):

    hli.sort()

    lenght = len(hli)

    ans = lenght - bisect.bisect_left(hli, k)

    return ans

def main():
    n, k = map(int, input().split())
    hli = list(map(int, input().split()))
    print(roller_coaster(n, k, hli))

if __name__ == '__main__':
    main()