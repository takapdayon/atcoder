def power_socket(a, b):

    ans = -(-(b-1)//(a-1))

    return ans

def main():
    a, b = map(int, input().split())
    print(power_socket(a, b))

if __name__ == '__main__':
    main()