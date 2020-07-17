def b170(x, y):

    for i in range(x+1):
        if 4*i + 2*(x-i) == y:
            return "Yes"

    return "No"

def main():
    x, y = map(int, input().split())
    print(b170(x, y))

if __name__ == '__main__':
    main()