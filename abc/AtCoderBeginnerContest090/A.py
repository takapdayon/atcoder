def Diagonal_String(c1, c2, c3):

    return c1[0] + c2[1] + c3[2]

def main():
    c1 = str(input())
    c2 = str(input())
    c3 = str(input())
    print(Diagonal_String(c1 , c2 , c3))

if __name__ == '__main__':
    main()