def DayofTaka(a , b):

    return a if a <= b else a - 1

def main():
    a , b = map(int , input().split())
    print(DayofTaka(a , b))

if __name__ == '__main__':
    main()