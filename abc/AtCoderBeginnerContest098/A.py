def Add_Sub_Mul(a , b):

    return max(a + b , a - b , a * b)

def main():
    a , b = map(int , input().split())
    print(Add_Sub_Mul(a , b))

if __name__ == '__main__':
    main()