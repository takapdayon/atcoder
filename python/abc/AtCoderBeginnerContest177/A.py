def a177(d, t, s):

    return "Yes" if d <= t*s else "No"

def main():
    d, t, s = map(int, input().split())
    print(a177(d, t, s))

if __name__ == '__main__':
    main()
