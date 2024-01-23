def dice_and_coin(n, k):

    ans = 0

    for i in range(1, n+1):
        count = i
        counter = 0
        while count < k:
            counter += 1
            count *= 2
        ans += 1/n * (1/2**counter)

    return ans

def main():
    n, k = map(int, input().split())
    print(dice_and_coin(n, k))

if __name__ == '__main__':
    main()