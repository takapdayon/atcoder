def b179(n, dlist):

    count = 0

    for i in dlist:
        if i[0] == i[1]:
            count += 1
        else:
            count = 0
        if 3 <= count:
            return "Yes"

    return "No"

def main():
    n = int(input())
    dlist = [list(map(int, input().split()))for i in range(n)]
    print(b179(n, dlist))

if __name__ == '__main__':
    main()
