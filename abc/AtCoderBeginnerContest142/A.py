def odds_of_oddness(n):

    return (n/2)/n if n%2 == 0 else int((n//2)+1)/n
def main():
    n = int(input())
    print(odds_of_oddness(n))

if __name__ == '__main__':
    main()
