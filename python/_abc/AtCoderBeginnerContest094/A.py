def Cats_Dogs(a , b , x):

    return "YES" if a <= x <= a + b else "NO"

def main():
    a , b , x = map(int , input().split())
    print(Cats_Dogs(a , b , x))

if __name__ == '__main__':
    main()