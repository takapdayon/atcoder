import math
def B_121(a , b):

    ans = "No"
    ab = a + b

    if int(math.sqrt(int(ab))) ** 2 == int(ab):
        ans = "Yes"

    return ans

def main():
    a , b = map(str , input().split())
    print(B_121(a , b))

if __name__ == '__main__':
    main()
