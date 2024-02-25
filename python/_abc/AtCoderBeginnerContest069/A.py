def kcity(n , m):

    return (n - 1) * (m - 1)

def main():
    n , m = map(int , input().split())
    print(kcity(n , m))

if __name__ == '__main__':
    main()