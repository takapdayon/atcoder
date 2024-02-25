def a176(n, x, t):

    return int(-(-n//x)*t)

def main():
    n, x, t = map(int, input().split())
    print(a176(n, x, t))

if __name__ == '__main__':
    main()