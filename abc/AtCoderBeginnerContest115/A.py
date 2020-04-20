def aChristmas(d):

    ans = "Christmas"
    return ans + " Eve"*abs(25-d)

def main():
    d = int(input())
    print(aChristmas(d))

if __name__ == '__main__':
    main()