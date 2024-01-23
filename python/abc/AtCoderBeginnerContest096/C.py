def Grid_Repainting(h , w , sl):

    ans = "Yes"
    xl = [1, 0, -1, 0]
    yl = [0 , 1 , 0 , -1]

    for i in range(h):
        for v in range(w):
            count = 0
            countcheck = 4
            if sl[i][v] == "#":
                for q in range(4):
                    x = i + xl[q]
                    y = v + yl[q]
                    if x >= 0 and x < h and y >= 0 and y < w:
                        if sl[x][y] == ".":
                            count += 1
                    else:
                        countcheck -= 1
            if count == countcheck:
                ans = "No"

    return ans

def main():
    h , w = map(int , input().split())
    sl = [list(str(input())) for i in range(h)]
    print(Grid_Repainting(h , w , sl))

if __name__ == '__main__':
    main()