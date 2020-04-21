def Right_Triangle(ab, bc, ca):

    return int(ab*bc/2)

def main():
    ab, bc, ca = map(int, input().split())
    print(Right_Triangle(ab, bc, ca))

if __name__ == '__main__':
    main()