
def RuinedSquare(x1 , y1 , x2 , y2):

    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)

    return str(x3) + " " + str(y3) + " " + str(x4) + " " + str(y4)

def main():
    x1 , y1 , x2 , y2 = map(int , input().split())
    print(RuinedSquare(x1 , y1 , x2 , y2))

if __name__ == '__main__':
    main()