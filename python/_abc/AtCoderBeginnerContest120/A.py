def favorite_sound(a, b, c):

    return c if b//a > c else b//a
def main():
    a, b, c = map(int, input().split())
    print(favorite_sound(a, b, c))

if __name__ == '__main__':
    main()