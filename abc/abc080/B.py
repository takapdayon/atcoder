def Harshad(n):

    count = 10
    sumn = 0
    while n // count > 0:
        sumn += (n // count) % 10
        count *= 10

    sumn += n % 10

    if n % sumn == 0:
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    print(Harshad(n))

if __name__ == '__main__':
    main()
