def a753(x):

    return "YES" if x == 3 or x == 5 or x == 7 else "NO"

def main():
    x = int(input())
    print(a753(x))

if __name__ == '__main__':
    main()