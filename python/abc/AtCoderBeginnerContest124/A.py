def buttons(a, b):

    return max(a, b) + max(max(a, b)-1,min(a, b))
def main():
    a, b = map(int, input().split())
    print(buttons(a, b))

if __name__ == '__main__':
    main()