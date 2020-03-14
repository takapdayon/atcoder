def goodinteger(s):

    ans = "No"

    for i in range(2):
        if s[i] == s[i + 1] and s[i] == s[i + 2]:
            ans = "Yes"

    return ans

def main():
    s = str(input())
    print(goodinteger(s))

if __name__ == '__main__':
    main()
