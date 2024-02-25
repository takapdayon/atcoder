def poor(a , b , c):

    s = {a , b , c}

    return "Yes" if len(s) == 2 else "No"
def main():
    a , b , c = map(int , input().split())
    print(poor(a , b , c))

if __name__ == '__main__':
    main()