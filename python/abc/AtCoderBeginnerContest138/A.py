def RedorNot(a , s):

    return s if a >= 3200 else "red"

def main():
    a = int(input())
    s = str(input())
    print(RedorNot(a , s))

if __name__ == '__main__':
    main()