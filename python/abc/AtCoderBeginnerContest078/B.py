def isu(x , y , z):

    ans = (x - z) // (y + z)

    return ans
def main():
    x , y , z = map(int , input().split())
    print(isu(x , y , z))


if __name__ == '__main__':
    main()