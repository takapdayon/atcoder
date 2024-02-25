def StringTransformation(s , t):

    taious = {}
    taiout = {}
    ans = "Yes"

    for i in range(len(s)):
        if t[i] in taiout.keys() and taiout[t[i]] != s[i]:
            ans = "No"
            break
        elif s[i] in taious.keys() and taious[s[i]] != t[i]:
            ans = "No"
            break
        else:
            taiout[t[i]] = s[i]
            taious[s[i]] = t[i]

    return ans

def main():
    s = str(input())
    t = str(input())
    print(StringTransformation(s , t))

if __name__ == '__main__':
    main()