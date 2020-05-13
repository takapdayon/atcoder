def fifty_fifty(s):

    count = set(s)
    return "Yes" if len(count) == 2 and s.count(list(count)[0]) == 2 and s.count(list(count)[1]) == 2 else "No"
def main():
    s = list(str(input()))
    print(fifty_fifty(s))

if __name__ == '__main__':
    main()
