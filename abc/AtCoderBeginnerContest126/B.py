def yymm_or_mmyy(s):

    ans = ""
    flag1 = False
    flag2 = False

    for i in range(1, 13):
        if s[0:2] == str(i).zfill(2):
            flag1 = True
        if s[2:4] == str(i).zfill(2):
            flag2 = True

    if flag1 and flag2:
        ans = "AMBIGUOUS"
    elif flag1:
        ans = "MMYY"
    elif flag2:
        ans = "YYMM"
    else:
        ans = "NA"

    return ans

def main():
    s = str(input())
    print(yymm_or_mmyy(s))

if __name__ == '__main__':
    main()