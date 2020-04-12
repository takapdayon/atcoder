
def a162(n):

    return "Yes" if n.count("7") else "No"

def main():
    n = str(input())
    print(a162(n))

if __name__ == '__main__':
    main()