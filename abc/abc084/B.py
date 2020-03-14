
def Postal_Code(a , b , s):

    ans = "No"

    if s[:a].isdecimal() and s[a+1:].isdecimal() and s[a] == '-':
        ans = "Yes"

    return ans

def main():
    a , b = map(int , input().split())
    s = str(input())
    print(Postal_Code(a , b , s))

if __name__ == '__main__':
    main()
