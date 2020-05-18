def exception_handling(n, ali, bli):

    bli.append(0)
    count = 0
    ans = 0

    for i in range(n):
        count = min(ali[i], bli[i])
        ans += count
        ali[i] -= count
        bli[i] -= count

        count = min(ali[i+1], bli[i])
        ans += count
        ali[i+1] -= count
        bli[i] -= count

    return ans

def main():
    n = int(input())
    ali = list(map(int, input().split()))
    bli = list(map(int, input().split()))
    print(exception_handling(n, ali, bli))

if __name__ == '__main__':
    main()