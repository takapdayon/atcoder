def b164(a, b, c, d):

    t = c // b
    o = a // d
    if c%b != 0:
        t += 1
    if a%d != 0:
        o += 1

    return "No" if t > o else "Yes"

def main():
    a, b, c, d = map(int, input().split())
    print(b164(a, b, c, d))

if __name__ == '__main__':
    main()