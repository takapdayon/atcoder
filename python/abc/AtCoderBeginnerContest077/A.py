def rotation(c , c2):

    return "YES" if c == c2[-1] + c2[1] + c2[0] else "NO"

def main():
    c = str(input())
    c2 = str(input())
    print(rotation(c , c2))

if __name__ == '__main__':
    main()