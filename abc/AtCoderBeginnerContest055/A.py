def xy(A):
    ans = (A*800) - ((A//15)*200)
    return ans

def main():
    A = int(input())
    print(xy(A))

if __name__ == '__main__':
    main()
