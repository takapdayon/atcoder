def airplane(p, q, r):

    return p+q+r-max(p,q,r)
def main():
    p, q, r = map(int, input().split())
    print(airplane(p, q, r))

if __name__ == '__main__':
    main()
