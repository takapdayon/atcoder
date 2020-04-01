def RatedforMe(r):

    return "ABC" if r < 1200 else "ARC" if r < 2800 else "AGC"

def main():
    r = int(input())
    print(RatedforMe(r))

if __name__ == '__main__':
    main()