def c161(n , k):

    return (min(k - (n % k) , (n % k)))

def main():
    n , k = map(int , input().split())
    print(c161(n , k))
if __name__ == '__main__':
    main()