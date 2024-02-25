import time
import random

mt = random.Random(0)  # シード0でメルセンヌツイスターの乱数生成器を初期化

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
