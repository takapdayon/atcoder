def white_cells(H, W, h, w):

    return (H-h) * (W-w)
def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(white_cells(H, W, h, w))

if __name__ == '__main__':
    main()