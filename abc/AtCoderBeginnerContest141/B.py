def tap_dance(s):

    ki = s[0::2]
    gu = s[1::2]
    ans = "Yes"

    if "L" in ki:
        ans = "No"
    if "R" in gu:
        ans = "No"

    return ans

def main():
    s = str(input())
    print(tap_dance(s))

if __name__ == '__main__':
    main()