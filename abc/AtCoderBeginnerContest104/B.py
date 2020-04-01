
def AcCepted(s):

    ans = "WA"

    if s[0] == "A" and s[2:-1].count("C") == 1:
        s = s.replace("C" , "c")
        if s[1:].islower():
            ans = "AC"

    return ans

def main():
    s = str(input())
    print(AcCepted(s))

if __name__ == '__main__':
    main()