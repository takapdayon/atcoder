def hati(n):

    for i in range(1, 10):
        for w in range(i, 10):
            if n == i*w:
                return "Yes"

    return "No"

def main():
    n = int(input())
    print(hati(n))

if __name__ == '__main__':
    main()