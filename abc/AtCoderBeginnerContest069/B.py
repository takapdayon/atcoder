def i18n(s):

    count = (len(s) - 2)

    return str(s[0]) + str(count) + str(s[-1])

def main():
    s = str(input())
    print(i18n(s))

if __name__ == '__main__':
    main()