def kangaru(x):
    count = 0
    i = 0
    while count < x:
        count += i
        i += 1
#    while count != x:
#        if count + (i * 2 + 1) <= x:
#            count += i
#        elif count + i == x:
#            count += i
#        i += 1
    return i - 1

def main():
    x = int(input())
    print(kangaru(x))

if __name__ == '__main__':
    main()
