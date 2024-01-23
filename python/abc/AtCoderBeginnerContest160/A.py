
def a160(s):

    ans = "No"
    
    if s[2] == s[3] and s[4] == s[5]:
        ans = "Yes"

    return ans

def main():
    s = str(input())
    print(a160(s))

if __name__ == '__main__':
    main()