def abc(a,b,c):
    
    return "YES" if a[-1] == b[0] and b[-1] == c[0] else "NO"
 
def main():
    a , b , c = map(str, input().split())
    print(abc(a , b , c))
 
if __name__ == '__main__':
    main()