
def Infinite_Coins(n , a):

    return "Yes" if (n % 500) <= a else "No"

def main():
    n = int(input())
    a = int(input())
    print(Infinite_Coins(n , a))

if __name__ == '__main__':
    main()
