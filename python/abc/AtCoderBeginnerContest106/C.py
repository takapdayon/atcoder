def To_Infinity(s , k):

    ans = ""

    s1 = s.lstrip("1")

    if k - (len(s) - len(s1)) > 0:
        ans = s1[0]
    else:
        ans = "1"

    return ans
def main():
    s = str(input())
    k = int(input())
    print(To_Infinity(s , k))

if __name__ == '__main__':
    main()