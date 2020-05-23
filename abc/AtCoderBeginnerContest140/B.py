def maximal_value(n, bli):

    ans = []
    ans.append(bli[0])

    for i in range(n-1):
        if bli[i] < ans[i]:
            ans[i] = bli[i]
        ans.append(bli[i])

    return sum(ans)

def main():
    n = int(input())
    bli = list(map(int, input().split()))
    print(maximal_value(n, bli))

if __name__ == '__main__':
    main()