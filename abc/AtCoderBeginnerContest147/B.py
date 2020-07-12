def palindrome(s):

    ans = 0

    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            ans += 1
    return ans

def main():
    s = list(str(input()))
    print(palindrome(s))

if __name__ == '__main__':
    main()