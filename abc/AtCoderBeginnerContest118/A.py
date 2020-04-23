def aplusb(a, b):

    return a+b if b%a == 0 else b-a
def main():
    a, b = map(int, input().split())
    print(aplusb(a, b))

if __name__ == '__main__':
    main()