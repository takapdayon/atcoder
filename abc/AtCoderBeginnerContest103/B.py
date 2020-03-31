def splitmozi(n , s):

    spmozi = ""
    s = list(map(str , s))

    for i in range(len(s)):
        spmozi += s[(-n) + i]

    return spmozi

def String_Rotation(s , t):

    ans = "No"
    for i in range(len(s)):
        spmozi = splitmozi(i , s)
        if spmozi == t:
            ans = "Yes"

    return ans

def main():
    s = str(input())
    t = str(input())
    print(String_Rotation(s , t))

if __name__ == '__main__':
    main()