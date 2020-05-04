def coloring_colorfully(s):

    ans = 0
    color = {"0":"1", "1":"0"}

    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            ans += 1
            s[i] = color[s[i]]

    return ans

def main():
    s = list(str(input()))
    print(coloring_colorfully(s))

if __name__ == '__main__':
    main()