def d166(x):

    a = 0
    b = 0

    if x == 0:
        return "1" + " " + "1"
    if x < 0:
        for i in range(10000):
            ax = x + i**5
            if ax > 0:
                a = -i
                for w in range(i):
                    if ax-(w**5) == 0:
                        b = -w
                        return str(a) + " " + str(b)
            else:
                a = -i
                for w in range(i):
                    if ax+(w**5) == 0:
                        b = w
                        return str(a) + " " + str(b)

    else:
        for i in range(10000):
            ax = x - i**5
            if ax < 0:
                a = i
                for w in range(i):
                    if ax+(w**5) == 0:
                        b = w
                        return str(a) + " " + str(b)
            else:
                a = i
                for w in range(i):
                    if ax-(w**5) == 0:
                        b = -w
                        return str(a) + " " + str(b)

def main():
    x = int(input())
    print(d166(x))
if __name__ == '__main__':
    main()