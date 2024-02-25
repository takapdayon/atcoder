def fiveHundredYenCoins(k, x):

    return "Yes" if 500*k >= x else "No"

def main():
    k, x = map(int, input().split())
    print(fiveHundredYenCoins(k, x))

if __name__ == '__main__':
    main()