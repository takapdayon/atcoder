def a171(a):

    return "A" if a.isupper() else "a"

def main():
    a = str(input())
    print(a171(a))

if __name__ == '__main__':
    main()