def dubious(s, t):

    ans = ""
    count = -2

    for i in range(len(s) - len(t) + 1):
        for w in range(len(t)):
            if str(s[i + w]) != "?" and s[i + w] != t[w]:
                break
            elif w == len(t) - 1:
                count = i

    if count == -2:
        ans = "UNRESTORABLE"
    else:
        for i in range(len(s)):
            if i < count or count + len(t) < i:
                ans += s[i]
            elif i == count:
                ans += t
        ans = ans.replace("?" , "a")

    return ans

def main():
    s = str(input())
    t = str(input())
    print(dubious(s , t))

if __name__ == '__main__':
    main()
