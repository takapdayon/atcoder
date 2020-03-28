def String_palind(s):

    ans = "No"
    scount = int((len(s) - 1) / 2)
    ecount = int((len(s) + 3) / 2)
    slen = s[:scount]
    elen = s[ecount - 1:]

    if s == s[::-1] and slen == slen[::-1] and elen == elen[::-1]:
        ans = "Yes"

    return ans

def main():
    s = str(input())
    print(String_palind(s))

if __name__ == '__main__':
    main()