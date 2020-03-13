def anordinarygame(s):

    flag = True
    count = 0
    while flag:
        for i in range(len(s)):
            if len(s) != i and i != 0 and str(s[i-1]) != str(s[i+1]):
                count += 1
                s.pop(i)
                continue
            elif len(s) == i:
                return "Second" if count % 2 == 0 else "First"
        if len(s) < 3:
            return "Second" if count % 2 == 0 else "First"

def main():
    s = list(str(input()))
    print(anordinarygame(s))

if __name__ == '__main__':
    main()