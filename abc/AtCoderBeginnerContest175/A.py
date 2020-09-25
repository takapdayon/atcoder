def a175(s):

    if s[1] != "S":
        return len(s.replace("S", ""))

    return 0 if len(s.replace("S", "")) == 0 else 1

def main():
    s = str(input())
    print(a175(s))

if __name__ == '__main__':
    main()