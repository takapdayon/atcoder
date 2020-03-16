
def Libra(a , b , c , d):

    ans = ""

    if a + b == c + d:
        ans = "Balanced"
    elif a + b > c + d:
        ans = "Left"
    else:
        ans = "Right"

    return ans

def main():
    a , b , c , d = map(int , input().split())
    print(Libra(a , b , c , d))

if __name__ == '__main__':
    main()
