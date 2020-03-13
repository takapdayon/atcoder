def notfound(s):

    for code in range(ord('a'), ord('z') + 1):
        if s.count(chr(code)) == 0:
            return chr(code)
    return "None"

def main():
    s = str(input())
    print(notfound(s))

if __name__ == '__main__':
    main()