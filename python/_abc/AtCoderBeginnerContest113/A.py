def DiscountFare(x , y):

    return int(x + (y / 2))

def main():
    x , y = map(int , input().split())
    print(DiscountFare(x , y))

if __name__ == '__main__':
    main()