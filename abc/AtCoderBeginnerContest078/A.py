def hex(x , y):

    ans = ""

    if int(x, 16) < int(y, 16):
        ans = "<"
    elif int(x, 16) > int(y, 16):
        ans = ">"
    else:
        ans = "="

    return ans

def main():
    x , y = map(str , input().split())
    print(hex(x , y))

if __name__ == '__main__':
    main()