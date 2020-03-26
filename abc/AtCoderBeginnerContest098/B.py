def CutandCount(n , s):

    ans = 0

    for i in range(1 , n + 1):
        count = 0
        for w in range(ord('a'), ord('z') + 1):
            if chr(w) in s[:i] and chr(w) in s[i:]:
                count += 1

        ans = max(ans , count)

    return ans

def main():
    n = int(input())
    s = str(input())
    print(CutandCount(n , s))

if __name__ == '__main__':
    main()