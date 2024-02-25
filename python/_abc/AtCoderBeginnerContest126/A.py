def changing_character(n, k, s):

    s[k-1] = s[k-1].lower()
    return "".join(s)
def main():
    n, k = map(int, input().split())
    s = list(str(input()))
    print(changing_character(n, k, s))

if __name__ == '__main__':
    main()