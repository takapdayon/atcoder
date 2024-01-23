def ball(s , t , a , b , u):

    if u == s:
        a -= 1
    else:
        b -= 1

    return str(a) + " " + str(b)

def main():
    s , t = map(str , input().split())
    a , b = map(int , input().split())
    u = str(input())
    print(ball(s , t , a , b , u))

if __name__ == '__main__':
    main()