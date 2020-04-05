def Train(n , i):

    return n - i + 1 if n != 1 else 1

def main():
    n , i = map(int , input().split())
    print(Train(n , i))

if __name__ == '__main__':
    main()