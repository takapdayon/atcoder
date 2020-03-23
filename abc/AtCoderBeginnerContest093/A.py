def abc_of_ABC(s):

    return "Yes" if s.count("a") == 1 and s.count("b") == 1 else "No"

def main():
    s = str(input())
    print(abc_of_ABC(s))

if __name__ == '__main__':
    main()