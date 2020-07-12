def roundone(a, b):

    abc = "123"

    return abc.replace(a, "").replace(b, "")

def main():
    a = str(input())
    b = str(input())
    print(roundone(a, b))

if __name__ == '__main__':
    main()