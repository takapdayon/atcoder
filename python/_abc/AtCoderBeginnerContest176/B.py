def b176(n):

    intn = [int(i) for i in n]

    return "Yes" if sum(intn) % 9 == 0 else "No"


def main():
    n = list(str(input()))
    print(b176(n))

if __name__ == '__main__':
    main()