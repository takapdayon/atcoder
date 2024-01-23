def parking(n , a , b):

    return b if n * a > b else n * a

def main():
    n , a , b = map(int , input().split())
    print(parking(n , a , b))

if __name__ == '__main__':
    main()
