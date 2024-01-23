def oddstring(s):

    ans = ""

    for i in range(0 , len(s) , 2):
        ans += s[i]

    return ans

def main():
    s = str(input())
    print(oddstring(s))

if __name__ == '__main__':
    main()