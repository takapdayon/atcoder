def changehi(n):

    return "Yes" if n[0] == n[-1] else "No"

def main():
    n = str(input())
    print(changehi(n))

if __name__ == '__main__':
    main()
