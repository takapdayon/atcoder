a, b, c = map(int, input().split())
if a == b:
    print('Takahashi' if c == 1 else 'Aoki')
else:
    print('Takahashi' if a > b else 'Aoki')