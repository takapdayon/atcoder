import time
import random
import math
random.seed(1)

class TimeKeeper:
    def __init__(self, time_threshold) -> None:
        self.time_threshold = time_threshold

        self.start_time = time.time()
        self.before_time = self.start_time

    def now_time(self):
        return time.time()

    def set_time(self):
        # 必要であれば、進めた情報をここで更新する
        self.before_time = time.time()

    def is_time_over(self):
        # 思考タイムが残っているか
        now = time.time()
        whole_diff = now - self.start_time
        whole_count = int(whole_diff * 1000)

        return whole_count >= self.time_threshold

class TempManager:
    def __init__(self, start_temp = 50, end_temp = 10) -> None:
        self.start_temp = start_temp
        self.end_temp = end_temp

    def temp(self, tk):
        return self.start_temp + (self.end_temp - self.start_temp) * ((tk.now_time() - tk.start_time) * 1000) / tk.time_threshold

    def probability(self, new, pre, temp):
        return math.exp((new - pre) / temp)

    def should_change(self, probability):
        return random.random() < probability

class State:
    def __init__(self) -> None:
        pass

    @classmethod
    def copy(cls):
        '''遷移関数'''

    pass

    def modify(state):
        pass

    def calc_score(state):
        pass

def sa():
    state = State()
    init(state)

    start_temp, end_temp = 100.0, 0.1  # Replace with appropriate values
    start_time = time.time()
    time_limit = 10.0  # Replace with the desired time limit

    while True:
        now_time = time.time()
        if now_time - start_time > time_limit:
            break

        new_state = State()
        modify(new_state)
        new_score = calc_score(new_state)
        pre_score = calc_score(state)

        # Temperature function
        temp = start_temp + (end_temp - start_temp) * (now_time - start_time) / time_limit

        # Transition probability function (for maximization)
        prob = math.exp((new_score - pre_score) / temp)

        if prob > random.uniform(0, 1):  # Transition with probability prob
            state = new_state