def batcoder(n , r):

    return r if n > 10 else r + 100 * (10 - n)

def main():
    n , r = map(int , input().split())
    print(batcoder(n , r))

if __name__ == '__main__':
    main()
