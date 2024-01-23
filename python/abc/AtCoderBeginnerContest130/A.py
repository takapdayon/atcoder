def rounding(x, a):

    return 0 if x < a else 10
def main():
    x, a = map(int, input().split())
    print(rounding(x, a))

if __name__ == '__main__':
    main()
