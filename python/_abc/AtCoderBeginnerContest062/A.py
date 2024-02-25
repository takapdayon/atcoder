def group(x , y):

    gx = 0
    gy = 0

    groups = [[1 , 3 , 5 , 7 , 8 , 10 , 12] , [4 , 6 , 9 , 11] , [2]]

    for i in range(3):
        if groups[i].count(x) != 0:
            gx = i
        if groups[i].count(y) != 0:
            gy = i

    return "Yes" if gx == gy else "No"

def main():
    x , y = map(int , input().split())
    print(group(x , y))
 
if __name__ == '__main__':
    main()