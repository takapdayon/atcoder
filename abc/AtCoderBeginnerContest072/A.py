def sandglass(x , t):

    return x - t if x - t > 0 else 0

def main():
    x , t = map(int , input().split())
    print(sandglass(x , t))

if __name__ == '__main__':
    main()
