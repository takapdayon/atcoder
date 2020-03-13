def writeanderase(n , a):

    ans = {}
    count = 0

    for i in range(n):
        if a[i] in ans:
            ans[a[i]] += 1
        else:
            ans[a[i]] = 1

    for i in ans.values():
        count += i % 2

    return count

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    print(writeanderase(n , a))

if __name__ == '__main__':
    main()