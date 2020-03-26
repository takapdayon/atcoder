def Attention(n , s):

    ans = 10**9
    west = [0] * (n + 1)
    east = [0] * (n + 1)

    for i in range(n):
        if s[i] == 'W':
            west[i + 1] = west[i] + 1
            east[i + 1] = east[i]
        else:
            west[i + 1] = west[i]
            east[i + 1] = east[i] + 1

    for i in range(n):
        count = west[i] + (east[-1] - east[i + 1])
        ans = min(ans , count)

    return ans

def main():
    n = int(input())
    s = list(str(input()))
    print(Attention(n , s))

if __name__ == '__main__':
    main()