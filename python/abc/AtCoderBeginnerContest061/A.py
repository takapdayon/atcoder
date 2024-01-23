def abc(a,b,c):

    return "Yes" if c >= a and c <= b else "No"

def main():
    a , b , c = map(int , input().split())
    print(abc(a , b , c))

if __name__ == '__main__':
    main()