def poll(n , s):

    ss = {}
    maxint = 0
    ans = []

    for i in range(n):
        if s[i] in ss:
            ss[s[i]] += 1
        else:
            ss[s[i]] = 1

    maxint = max(ss.values())

    ans = [k for k, v in ss.items() if v == maxint]

    ans.sort()
    return ans

def main():
    n = int(input())
    s =[str(input()) for i in range(n)]
    ans = poll(n , s)

    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()