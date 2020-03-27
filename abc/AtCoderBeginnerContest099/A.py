def ABD(n):

    return "ABC" if n / 1000 < 1 else "ABD"

def main():
    n = int(input())
    print(ABD(n))

if __name__ == '__main__':
    main()