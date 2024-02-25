def a164(s, w):

    return "unsafe" if s <= w else "safe"
def main():
    s, w = map(int, input().split())
    print(a164(s, w))

if __name__ == '__main__':
    main()