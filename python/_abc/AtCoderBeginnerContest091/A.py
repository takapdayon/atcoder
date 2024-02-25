def Two_Coins(a , b , c):

    return "Yes" if a + b >= c else "No"

def main():
    a , b , c = map(int , input().split())
    print(Two_Coins(a , b , c))

if __name__ == '__main__':
    main()