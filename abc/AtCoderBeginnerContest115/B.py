def bChristmas(n, pl):

    return int(sum(pl) - (max(pl)/ 2))

def main():
    n = int(input())
    pl = [int(input()) for i in range(n)]
    print(bChristmas(n, pl))

if __name__ == '__main__':
    main()
