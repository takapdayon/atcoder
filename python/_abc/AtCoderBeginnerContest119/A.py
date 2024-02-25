def still_tdb(s):

    return "Heisei" if s <= "2019/04/30" else "TBD"
def main():
    s = str(input())
    print(still_tdb(s))

if __name__ == '__main__':
    main()