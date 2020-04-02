
def BaseNumber(n):

    ans = ""

    if n == 0:
        ans = "0"

    return ans
def main():
    n = int(input())
    print(BaseNumber(n))

if __name__ == '__main__':
    main()