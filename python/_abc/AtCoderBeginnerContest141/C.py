def attack_survival(n, k, q, ali):

    count = [0]*n
    ans = []

    for i in ali:
        count[i-1] += 1

    for i in range(n):
        if k+count[i]-q > 0:
            ans.append("Yes")
        else:
            ans.append("No")

    return ans

def main():
    n, k, q = map(int, input().split())
    ali = [int(input())for i in range(q)]
    ans = attack_survival(n, k, q, ali)
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()