def b168(k, s):

    if k >= len(s):
        return s
    else:
        return s[:k] + "..."

def main():
    k = int(input())
    s = str(input())
    print(b168(k, s))

if __name__ == '__main__':
    main()