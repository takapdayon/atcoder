def SomethingIt(s):

    return 700 + (s.count("o") * 100)

def main():
    s = list(str(input()))
    print(SomethingIt(s))

if __name__ == '__main__':
    main()