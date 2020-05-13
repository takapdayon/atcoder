def rectangle_cutting(w, h, x, y):

    a = 0
    ans = (w*h) / 2

    if x*2 == w and y*2 == h:
        a = 1

    return ans, a
def main():
    w, h, x, y = map(int, input().split())
    print(*(rectangle_cutting(w, h, x, y)))

if __name__ == '__main__':
    main()