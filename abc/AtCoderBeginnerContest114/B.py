def b754(s):

    ans = 10**7

    for i in range(len(s) - 2):
        ans = min(ans , abs(int(s[i:i+3]) - 753))

    return ans

def main():
    s = str(input())
    print(b754(s))

if __name__ == '__main__':
    main()
