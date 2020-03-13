def eatperiod(x , a , b):

    ans = ""

    if (b - a) >= (x + 1):
        ans = "dangerous"
    elif (b - a) > 0:
        ans = "safe"
    else:
        ans = "delicious"

    return ans

def main():
    x , a , b = map(int , input().split())
    print(eatperiod(x , a , b))

if __name__ == '__main__':
    main()