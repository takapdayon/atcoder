def anordinarygame(s):

    ans = ""
    if s[0] == s[-1]:
        ans = "Second" if len(s) % 2 else "First"
    else:
        ans = "First" if len(s) % 2 else "Second"

    return ans

def main():
    s = list(str(input()))
    print(anordinarygame(s))

if __name__ == '__main__':
    main()