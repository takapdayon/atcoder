import math

def plusup(a , b):

    return math.ceil((a + b) / 2)

def main():
    a , b = map(int , input().split())
    print(plusup(a , b))

if __name__ == '__main__':
    main()
