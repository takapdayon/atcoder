def Eating(s):

    return s.count("+") - s.count("-")

def main():
    s = str(input())
    print(Eating(s))

if __name__ == '__main__':
    main()