def Dimensional(n , m , x , y , xl , yl):

    ans = "War"

    xmax = max(xl) + 1
    ymin = min(yl)

    if xmax <= ymin and x < ymin and xmax < y:
        ans = "No War"

    return ans

def main():
    n , m , x , y = map(int , input().split())
    xl = list(map(int , input().split()))
    yl = list(map(int , input().split()))
    print(Dimensional(n , m , x , y , xl , yl))

if __name__ == '__main__':
    main()