import time
import random

random.seed(1)

# def rand_xor():
#     global x, y, z, w
#     x = 123456789
#     y = 362436069
#     z = 521288629
#     w = 88675123

#     t = x ^ (x << 11)
#     x = y
#     y = z
#     z = w
#     w = (w ^ (w >> 19)) ^ (t ^ (t >> 8))
#     return w

# def rand01():
#     return (rand_xor() + 0.5) * (1.0 / (2**32))

class TimeKeeper:
    def __init__(self, time_threshold) -> None:
        self.time_threshold = time_threshold

        self.start_time = time.time()
        self.before_time = self.start_time

    def set_turn(self, turn):
        self.turn = turn
        self.before_time = time.time()

    def set_some(self, some):
        # 必要であれば、進めた情報をここで更新する
        self.before_time = time.time()

    def is_time_over(self):
        # 思考タイムが残っているか
        now = time.time()
        whole_diff = now - self.start_time
        whole_count = int(whole_diff * 1000)
        last_diff = now - self.before_time
        last_count = int(last_diff * 1000)

        remaining_time = self.time_threshold - whole_count
        now_threshold = remaining_time / (TURN - self.turn)
        return last_count >= now_threshold

class State:
    def __init__(self, candies) -> None:
        self.t = 0
        self.board = [[0] * W for _ in range(H)]
        self.candies = candies

    @classmethod
    def copy(cls, source):
        instance = cls(source.candies)
        instance.board = [row[:] for row in source.board]
        instance.t = source.t
        return instance

    def is_done(self):
        return self.t >= TURN

    def advance(self, action):
        # キャンディを一つ進める
        if action == F:
            for x in range(W):
                dest = 0
                for y in range(dest, H):
                    if self.board[y][x] != 0:
                        self.board[dest][x], self.board[y][x] = self.board[y][x], self.board[dest][x]
                        dest += 1
        elif action == B:
            for x in range(W):
                dest = H - 1
                for y in range(dest, -1, -1):
                    if self.board[y][x] != 0:
                        self.board[dest][x], self.board[y][x] = self.board[y][x], self.board[dest][x]
                        dest -= 1
        elif action == L:
            for y in range(H):
                dest = 0
                for x in range(dest, W):
                    if self.board[y][x] != 0:
                        self.board[y][dest], self.board[y][x] = self.board[y][x], self.board[y][dest]
                        dest += 1
        elif action == R:
            for y in range(H):
                dest = W - 1
                for x in range(dest, -1, -1):
                    if self.board[y][x] != 0:
                        self.board[y][dest], self.board[y][x] = self.board[y][x], self.board[y][dest]
                        dest -= 1
        self.t += 1

    def random_update(self):
        reverse_t = TURN - self.t
        if reverse_t == 0:
            return
        p = mt.randint(1, reverse_t)
        pos = 0
        for h in range(H):
            for w in range(W):
                if self.board[h][w] == 0:
                    p -= 1
                if p == 0:
                    pos = h * 10 + w
                    break
        self.update(pos)

    def update(self, pt):
        h = pt // W
        w = pt % W
        self.board[h][w] = self.candies[self.t]

    def get_score(self):
        score = 0
        checked = [[0] * W for _ in range(H)]
        for h in range(H):
            for w in range(W):
                if self.board[h][w] != 0 and not checked[h][w]:
                    group_size = self._get_group_size(h, w, checked)
                    score += group_size * group_size
        return score

    def _get_group_size(self, h, w, checked):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        candy = self.board[h][w]
        checked[h][w] = True

        q = deque([(h, w)])
        cnt = 0
        while q:
            cnt += 1
            now_y, now_x = q.popleft()
            for di in range(4):
                ty = now_y + dy[di]
                tx = now_x + dx[di]
                if 0 <= ty < H and 0 <= tx < W and not checked[ty][tx] and self.board[ty][tx] == candy:
                    checked[ty][tx] = True
                    q.append((ty, tx))
        return cnt


def play_1turn():
    # 1ターンプレイするのに必要なadvance要素をランダムに返す
    pass

def playout(state):
    '''
    is_doneとなるまでシミュレーションを続ける
    ランダム値はplay_1turnから取得する。
    '''
    # is_doneになるまで
    state.advance(play_1turn())
    while not state.is_done():
        state.random_update()
        state.advance(play_1turn())
    return state.get_score()

def primitive_montecalro(time_keeper, base_state):
    '''
    シミュレーションを実行する
    シミュレーションの結果、一番良かった結果を返却する
    '''
    pass
