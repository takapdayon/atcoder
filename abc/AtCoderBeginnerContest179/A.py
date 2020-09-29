def a179(s):

    return s+"s" if s[-1] != "s" else s+"es"

def main():
    s = str(input())
    print(a179(s))

if __name__ == '__main__':
    main()