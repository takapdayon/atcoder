def a173(n):

    return 1000-int(n[-3:]) if int(n[-3:]) != 0 else 0

def main():
    n = str(input())
    print(a173(n))

if __name__ == '__main__':
    main()