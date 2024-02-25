def ferris_wheel(a, b):

    return b if 13<=a else int(b/2) if 6<= a<=12 else 0
def main():
    a, b = map(int, input().split())
    print(ferris_wheel(a, b))

if __name__ == '__main__':
    main()