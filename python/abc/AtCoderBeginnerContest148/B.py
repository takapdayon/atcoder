def stringWithTheSameLength(n, s, t):

    ans = ""

    for i in range(n):
        ans += s[i] + t[i]

    return ans

def main():
    n = int(input())
    s, t = map(str, input().split())
    print(stringWithTheSameLength(n, s, t))

if __name__ == '__main__':
    main()