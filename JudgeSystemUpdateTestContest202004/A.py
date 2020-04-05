
def ajsut(x , y , z):

    ans = 0

    if y <= x <= z:
        ans = x
    elif x > z:
        ans = z
    else:
        ans = y
    
    return ans

def main():
    x , y , z = map(int , input().split())
    print(ajsut(x , y , z))

if __name__ == '__main__':
    main()