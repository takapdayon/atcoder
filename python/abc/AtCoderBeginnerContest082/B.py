
def Two_Anagrams(s , t):

    ans = ""
    s.sort()
    t.sort(reverse=True)

    for i in range(min(len(s) , len(t))):
        if s[i] > t[i]:
            ans = "No"
            break
        elif s[i] < t[i]:
            ans = "Yes"
            break

    if not ans and len(s) >= len(t):
        ans = "No"
    elif not ans:
        ans = "Yes"

    return ans

def main():
    s = list(str(input()))
    t = list(str(input()))
    print(Two_Anagrams(s , t))

if __name__ == '__main__':
    main()
