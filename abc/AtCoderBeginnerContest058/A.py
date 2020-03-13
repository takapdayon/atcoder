def ntukusi(a,b,c):
    return "YES" if (b - a) == (c - b) else "NO"
 
def main():
    a , b , c = map(int, input().split())
    print(ntukusi(a , b , c))
 
if __name__ == '__main__':
    main()