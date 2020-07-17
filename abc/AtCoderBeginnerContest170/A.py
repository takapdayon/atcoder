def a170(x):

    for index, i in enumerate(x):
        if i == 0:
            return index+1

def main():
    x = list(map(int, input().split()))
    print(a170(x))

if __name__ == '__main__':
    main()