def tenki(s, t):

    ans = 0

    for i in range(len(s)):
        if s[i] == t[i]:
            ans += 1

    return ans

def main():
    s = list(str(input()))
    t = list(str(input()))
    print(tenki(s, t))

if __name__ == '__main__':
    main()