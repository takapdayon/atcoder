
def Already2018(s):

    ans = s[:3] + '8' + s[4:]
    return ans

def main():
    s = str(input())
    print(Already2018(s))

if __name__ == '__main__':
    main()
