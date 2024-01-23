def abc(a,b,c):
    return (a[0] + b[0] + c[0]).upper()
 
def main():
    a , b , c = map(str, input().split())
    print(abc(a , b , c))
 
if __name__ == '__main__':
    main()