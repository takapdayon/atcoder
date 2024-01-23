def strings(s, t):

    return t+s

def main():
    s, t = map(str, input().split())
    print(strings(s, t))

if __name__ == '__main__':
    main()