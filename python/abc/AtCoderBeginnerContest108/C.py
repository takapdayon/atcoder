#要復習
def Triangular(n , k):
    ans = 0

    if k % 2 == 1:
        ans = (n // k)**3
    else:
        ans = (n // k)**3 + (((k / 2) + n) // k)**3

    return int(ans)

def main():
    n , k = map(int , input().split())
    print(Triangular(n , k))

if __name__ == '__main__':
    main()