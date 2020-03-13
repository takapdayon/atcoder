def hd(a,b):
    ans = ""
    if a == "H":
        ans = "H" if b == "H" else "D"
    else:
        ans = "D" if b == "H" else "H"

    return ans

def main():
    a , b = map(str, input().split())
    print(hd(a , b))

if __name__ == '__main__':
    main()
