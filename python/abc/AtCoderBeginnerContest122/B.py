def atcoder(s):

    ans = 0
    count = 0
    acgt = ["A", "C", "G", "T"]

    for i in s:
        if i in acgt:
            count += 1
        else:
            count = 0
        ans = max(ans, count)
    return ans

def main():
    s = list(str(input()))
    print(atcoder(s))

if __name__ == '__main__':
    main()