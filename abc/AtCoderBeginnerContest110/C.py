def StringTransformation(s , t):

    for i in range(len(s)):
        s.replace(s[i] , t[i])

    return "Yes" if s == t else "No"

def main():
    s = str(input())
    t = str(input())
    print(StringTransformation(s , t))

if __name__ == '__main__':
    main()