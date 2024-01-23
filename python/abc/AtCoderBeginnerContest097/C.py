def Kth_Substring(s , k):

    ans = []
    sset = set()

    for i in range(len(s)):
        for w in range(1, k + 1):
            sset.add(s[i:i + w])
    ans = sorted(list(sset))
    return ans[k - 1]

def main():
    s = str(input())
    k = int(input())
    print(Kth_Substring(s , k))

if __name__ == '__main__':
    main()