def security(s):

    return "Good" if s[0] != s[1] and s[1] != s[2] and s[2] != s[3] else "Bad"
def main():
    s = list(str(input()))
    print(security(s))

if __name__ == '__main__':
    main()
