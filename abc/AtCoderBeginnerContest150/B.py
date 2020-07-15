def countABC(n, s):

    return s.count("ABC")

def main():
    n = int(input())
    s = str(input())
    print(countABC(n, s))

if __name__ == '__main__':
    main()