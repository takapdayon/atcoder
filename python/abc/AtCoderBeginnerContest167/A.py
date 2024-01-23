def a167(s, t):

    return "Yes" if s == t[:-1] else "No"
def main():
    s = str(input())
    t = str(input())
    print(a167(s, t))

if __name__ == '__main__':
    main()