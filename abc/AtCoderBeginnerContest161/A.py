
def a161(x , y , z):

    return z + " " + x + " " + y

def main():
    x , y , z = map(str , input().split())
    print(a161(x , y , z))

if __name__ == '__main__':
    main()