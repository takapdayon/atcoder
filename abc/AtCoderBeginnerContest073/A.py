def september9(n):

    return "Yes" if n[0] == "9" or n[-1] == "9" else "No"

def main():
    n = str(input())
    print(september9(n))

if __name__ == '__main__':
    main()