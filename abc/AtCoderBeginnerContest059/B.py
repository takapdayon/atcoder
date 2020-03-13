def gle(a , b):
    ans = ""
    if a == b:
        ans = "EQUAL"
    elif a > b:
        ans = "GREATER"
    else:
        ans = "LESS"
    return ans

def main():
    a = int(input())
    b = int(input())
    print(gle(a , b))

if __name__ == '__main__':
    main()
