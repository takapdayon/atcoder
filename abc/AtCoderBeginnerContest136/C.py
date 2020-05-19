def build_stairs(n, hli):

    ans = "Yes"

    for i in range(1, n):
        if hli[i-1] < hli[i]:
            hli[i] -= 1
        elif hli[i-1] == hli[i]:
            pass
        else:
            return "No"

    return ans

def main():
    n = int(input())
    hli = list(map(int, input().split()))
    print(build_stairs(n, hli))

if __name__ == '__main__':
    main()