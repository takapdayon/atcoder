def biscuit_generator(a, b, t):

    return (t//a) * b
def main():
    a, b, t = map(int, input().split())
    print(biscuit_generator(a, b, t))

if __name__ == '__main__':
    main()