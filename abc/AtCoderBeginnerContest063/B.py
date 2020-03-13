def differentcount(s):

    for i in range(len(s)):
        if s.count(s[i]) != 1:
            return "no"

    return "yes"

def main():
    s = str(input())
    print(differentcount(s))

if __name__ == '__main__':
    main()