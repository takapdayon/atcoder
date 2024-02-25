
def b(al , n , nl):

    ans = "No"

    n = [[False]*3 for i in range(3)]

    for i in range(3):
        for w in range(3):
            if al[i][w] in nl:
                n[i][w] = True
    
    for i in range(3):
        if n[i][0] == True and n[i][1] == True and n[i][2] == True:
            ans = "Yes"
    
    for i in range(3):
        if n[0][i] == True and n[1][i] == True and n[2][i] == True:
            ans = "Yes"
    
    if n[0][0] == True and n[1][1] == True and n[2][2] == True:
        ans = "Yes"
    if n[0][2] == True and n[1][1] == True and n[2][0] == True:
        ans = "Yes"

    return ans

def main():
    al = [list(map(int , input().split())) for i in range(3)]
    n = int(input())
    nl = [int(input()) for i in range(n)]
    print(b(al , n , nl))

if __name__ == '__main__':
    main()
