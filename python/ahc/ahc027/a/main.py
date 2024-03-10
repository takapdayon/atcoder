import random
import sys
from time import perf_counter
import argparse
from collections import deque

sys.setrecursionlimit(5*10**5)

class TimeKeeper:
    def __init__(self):
        self.start_time = perf_counter()
    def is_time_over(self, LIMIT):
        return (perf_counter() - self.start_time) >= LIMIT
    def time_now(self):
        return (perf_counter() - self.start_time)

def make_kmp_table(t):
    i = 2
    j = 0
    m = len(t)
    tbl = [0] * (m + 1)
    tbl[0] = -1
    while i <= m:
        if t[i - 1] == t[j]:
            tbl[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = tbl[j]
        else:
            tbl[i] = 0
            i += 1
    return tbl
 
def kmp(s, t):
    matched_indices = []
    tbl = make_kmp_table(t)
    i = 0
    j = 0
    n = len(s)
    m = len(t)
    while i + j < n:
        if t[j] == s[i + j]:
            j += 1
            if j == m:
                matched_indices.append(i)
                i += j - tbl[j]
                j = tbl[j]
        else:
            i += j - tbl[j]
            if j > 0:
                j = tbl[j]
    return matched_indices

###############################
def main(DEBUG):
    global tnow, cnt_visited
    time_keeper = TimeKeeper()

    N = int(input())
    h = [input() for _ in range(N-1)]
    v = [input() for _ in range(N)]
    d = [list(map(int, input().split())) for _ in range(N)]
    dij = []
    DSUM = 0
    for i in range(N):
        for j in range(N):
            DSUM += d[i][j]
            dij.append((d[i][j], i, j))
    dij.sort(reverse=True)

    DIJ = [(0,1), (1,0), (0,-1), (-1,0)]
    DIR = "RDLU"
    to_dij = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
    to_dir = {"R": 0, "D": 1, "L": 2, "U": 3}
    to_DIR = {(0, 1):"R", (1, 0):"D", (0, -1):"L" , (-1, 0):"U"}
    
    movable = [[[] for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            for dir in range(4):
                di, dj = DIJ[dir]
                i2 = i + di
                j2 = j + dj
                if 0 <= i2 < N and 0 <= j2 < N:
                    if (di == 0 and v[i][min(j, j2)] == '0') or (dj == 0 and h[min(i, i2)][j] == '0'):
                        movable[i][j].append(dir)

    
    def cal_score(ANS, all=False):
        sc = 0
        L = len(ANS)
        i, j = 0, 0
        visit_time = [[[] for _ in range(N)] for _ in range(N)]
        for t, item in enumerate(ANS):
            if all == True:
                _, _, _, c = item
            else:
                c = item
            di, dj = to_dij[c]
            dir = to_dir[c]
            if dir not in movable[i][j]:
                sc = 10**18
                return sc
            i += di
            j += dj
            # print(i, j)
            visit_time[i][j].append(t)
        for i in range(N):
            for j in range(N):
                nt = len(visit_time[i][j])
                if nt == 0:
                    sc = 10**18
                    return sc
                if nt == 1:
                    sc_ = L * (L-1) * d[i][j] // 2
                else:
                    sc_ = 0
                    for k in range(nt):
                        T = (visit_time[i][j][k] - visit_time[i][j][k-1]) % L
                        sc_ += T * (T-1)
                    sc_ = sc_ * d[i][j] // 2
                sc += sc_
        sc = int((sc / L) + 0.5)
        return sc

    def search_dirtiest(inow, jnow):
        global tnow
        mx = -1
        for i in range(N):
            for j in range(N):
                if (i, j) == (inow, jnow):
                    continue
                dval = (1 + tnow - last_visited[i][j]) * d[i][j]
                if dval > mx:
                    mx = dval
                    imx, jmx = i, j
        return imx, jmx

    def cal_eval(i, j):
        eval_a = (tnow - last_visited[i][j]) * d[i][j]
        eval_dist = CDIST * dist_to_target[i][j] + CDIST * dist_to_target[i][j] ** 2 // 15
        eval_not_visited = CVISIT * (1 - visited[i][j])
        eval_nxt = 0
        for dir in movable[i][j]:
            di, dj = DIJ[dir]
            i2 = i + di
            j2 = j + dj
            eval_nxt_a = (tnow + 1 - last_visited[i2][j2]) * d[i2][j2]
            eval_nxt_dist = CDIST * dist_to_target[i2][j2] // 5
            eval_nxt_not_visited = CVISIT * (1 - visited[i2][j2])
            tmp = eval_nxt_a + eval_nxt_dist + eval_nxt_not_visited
            if tmp > eval_nxt:
                eval_nxt = tmp
        eval = int(eval_a + eval_dist + eval_not_visited + eval_nxt * CNXT)
        return eval

    def goto_eval(i, j, ito, jto):
        global tnow, cnt_visited
        move_log = []
        while (i, j) != (ito, jto):
            mx_eval = -10**9
            for dir in movable[i][j]:
                di, dj = DIJ[dir]
                i2 = i + di
                j2 = j + dj
                eval = cal_eval(i2, j2)
                if eval > mx_eval:
                    mx_eval = eval
                    mx_dir = dir
            # 更新
            di, dj = DIJ[mx_dir]
            i += di
            j += dj
            tnow += 1
            last_visited[i][j] = tnow
            if visited[i][j] == False:
                cnt_visited += 1
            visited[i][j] = True
            move_log.append(DIR[mx_dir])
        return move_log, i, j

    def BFS(ito, jto):
        que = deque()
        seen = [[False for _ in range(N)] for _ in range(N)]
        dist = [[10**18] * N for _ in range(N)]
        seen[ito][jto] = True
        dist[ito][jto] = 0
        que.append((ito, jto))
        while len(que) > 0:
            i, j = que.popleft()
            for dir in movable[i][j]:
                di, dj = DIJ[dir]
                i2 = i + di
                j2 = j + dj
                if not seen[i2][j2]:
                    seen[i2][j2] = True
                    dist[i2][j2] = dist[i][j] + 1
                    que.append((i2, j2))
        return dist

    def moveBFS(ist, jst, ito, jto):
        que = deque()
        seen = [[False for _ in range(N)] for _ in range(N)]
        dist = [[10**18] * N for _ in range(N)]
        prev = [[(-1, -1)] * N for _ in range(N)]
        seen[ist][jst] = True
        dist[ist][jst] = 0
        que.append((ist, jst))
        while len(que) > 0:
            i, j = que.popleft()
            if (i, j) == (ito, jto):
                break
            for dir in movable[i][j]:
                di, dj = DIJ[dir]
                i2 = i + di
                j2 = j + dj
                if not seen[i2][j2]:
                    seen[i2][j2] = True
                    dist[i2][j2] = dist[i][j] + 1
                    prev[i2][j2] = (i, j)
                    que.append((i2, j2))
        def get_path(end):
            path = []
            while end != (-1, -1):
                path.append(end)
                end = prev[end[0]][end[1]]
            path.reverse()
            return path
        path = get_path((ito, jto))
        return path

    def dist_from_target(ito, jto):
        if (ito, jto) in setBFS:
            dist_ = dictBFS[(ito, jto)]
        else:
            dist_ = BFS(ito, jto)
            setBFS.add((ito, jto))
            dictBFS[(ito, jto)] = dist_
        return dist_

    def dfs_insert(i, j, t, path):
        # 隣接セルで未訪問地点があればパスに追加する
        global cnt_visited
        for dir in movable[i][j]:
            di, dj = DIJ[dir]
            i2 = i + di
            j2 = j + dj
            if visit_count[i2][j2] == 0:
                cnt_visited += 1
                path.insert(t+1, (i2, j2))
                path.insert(t+2, (i, j))
                last_visited[i2][j2] = t+1
                visited[i2][j2] = True
                visit_count[i2][j2] += 1
                visit_count[i][j] += 1
                dfs_insert(i2, j2, t+1, path)

   
    #############################################
    # 時間のある限りまわす
    if DEBUG == True:
        LIMIT1 = 1.2
        LIMIT2 = 1.65
        LIMIT3 = 1.75
    else:
        LIMIT1 = 1.2
        LIMIT2 = 1.65
        LIMIT3 = 1.75

    bestsc = 10**18 # 小さい方が良い
    best_last_visited = [[0] * N for _ in range(N)] #* ループ１回目のみゼロ初期化
    loop = 0
    setBFS = set()
    dictBFS = dict()

    ############
    # 初期パラメータ
    CDIST = -1000
    CVISIT = 10**5
    CNXT = 0.5
    MXITER = 10**6
    MXT    = 3 * N**2
    BESTPARA = [CDIST, CVISIT, CNXT, MXITER, MXT]

    while True:
        if time_keeper.is_time_over(LIMIT1):
            print(f"loop: {loop}", file=sys.stderr)
            break
        loop += 1

        ############
        # パラメータ
        CDIST = int(BESTPARA[0] * random.gauss(1.0, 0.5))
        CDIST = min(CDIST, -100)
        CVISIT = int(BESTPARA[1] * random.uniform(1.0, 0.5))
        CVISIT = max(CVISIT, 10**3)
        CNXT = BESTPARA[2] * random.uniform(0.99, 1.01)
        MXT = int(BESTPARA[4] * random.gauss(1.0, 0.2))

        ############
        # 初期化
        ANS = []
        visited = [[False for _ in range(N)] for _ in range(N)]
        # last_visited = [[0] * N for _ in range(N)] # ループ１回目のみゼロ初期化
        last_visited = [list(sublist) for sublist in best_last_visited]

        cnt_visited = 0
        tnow = 0
        inow, jnow = 0, 0

        #########
        for iloop in range(MXITER):
            if tnow > MXT:
                break
            #########
            # 目的地決め
            ito, jto = search_dirtiest(inow, jnow)
            dist_to_target = dist_from_target(ito, jto)
            MOVE, inow, jnow = goto_eval(inow, jnow, ito, jto)
            ANS.extend(MOVE)

        #########
        # 原点へ帰る
        ito, jto = 0, 0
        dist_to_target = dist_from_target(ito, jto)
        MOVE, inow, jnow = goto_eval(inow, jnow, ito, jto)
        ANS.extend(MOVE)

        #########
        # 未訪問地点をパスに割り込ませる
        path = [(0, 0)]
        visit_count = [[0] * N for _ in range(N)]
        i, j = 0, 0
        for c in ANS:
            di, dj = to_dij[c]
            dir = to_dir[c]
            visit_count[i][j] += 1
            i += di
            j += dj
            path.append((i, j))
        # 未訪問地点がなくなるまで
        while cnt_visited < N**2:
            for t, (i, j) in enumerate(path):
                dfs_insert(i, j, t, path)
                if cnt_visited == N**2:
                    break
        # ANSを作り直す
        ANS = []
        for t in range(len(path)-1):
            i, j = path[t]
            i2, j2 = path[t+1]
            di, dj = i2-i, j2-j
            ANS.append(to_DIR[(di, dj)])

        # スコア計算
        sc = cal_score(ANS)
        if sc < bestsc:
            print(f" {loop} {sc} {CDIST} {CVISIT} {CNXT:.2f} {MXITER} {MXT}", file=sys.stderr)
            bestsc = sc
            bestANS = ANS[:]
            BESTPARA = [CDIST, CVISIT, CNXT, MXITER, MXT]
            best_last_visited = [list(l) for l in last_visited]
            tot_time = len(ANS)
            best_last_visited = [[x - tot_time for x in row] for row in best_last_visited]


    def improve(ANS_all, bestsc, T_LIMIT):
        # パス短縮による改善
        Lcut1 = ["LUR", "LDR", "RUL", "RDL", "ULD", "URD", "DLU", "DRU"]
        Lcut2 = ["LR", "RL", "UD", "DU"]
        endflag = False
        cnt = 0
        while endflag == False:
            cnt += 1
            print("imporove", cnt, file=sys.stderr)
            endflag = True
            for Lcut in Lcut1:
                t_match1 = kmp(bestANS, Lcut)
                for t in reversed(t_match1):
                    if time_keeper.is_time_over(T_LIMIT):
                        print("timeover:", file=sys.stderr)
                        return ANS_all, bestsc
                    i, j, dir, c = ANS_all[t][0], ANS_all[t][1], ANS_all[t][2], ANS_all[t][3]
                    dir2, c2 = ANS_all[t+1][2], ANS_all[t+1][3]
                    # 壁で移動できない場合は却下
                    if dir2 not in movable[i][j]:
                        continue
                    # 省略すると未到達セルが生じる場合も却下
                    di1, dj1 = to_dij[c]
                    di2, dj2 = to_dij[c2]
                    i1, j1 = i+di1, j+dj1
                    i2, j2 = i1+di2, j1+dj2
                    if visit_count[i1][j1] == 1 or visit_count[i2][j2] == 1:
                        continue
                    # スコアが改善されれば更新
                    sc = cal_score(ANS_all[:t] + [ANS_all[t+1]] + ANS_all[t+3:], all=True)
                    if sc < bestsc:
                        bestANS.pop(t)
                        bestANS.pop(t+1)
                        ANS_all.pop(t)
                        ANS_all.pop(t+1)
                        bestsc = sc
                        visit_count[i1][j1] -= 1
                        visit_count[i2][j2] -= 1
                        endflag = False
                        print("tempsc1:", t, Lcut, sc, file=sys.stderr)
                        continue
            for Lcut in Lcut2:
                t_match2 = kmp(bestANS, Lcut)
                for t in reversed(t_match2):
                    if time_keeper.is_time_over(T_LIMIT):
                        print("timeover:", file=sys.stderr)
                        return ANS_all, bestsc
                    i, j, dir, c = ANS_all[t][0], ANS_all[t][1], ANS_all[t][2], ANS_all[t][3]
                    dir2, c2 = ANS_all[t+1][2], ANS_all[t+1][3]
                    # 省略すると未到達セルが生じる場合も却下
                    di1, dj1 = to_dij[c]
                    i1, j1 = i+di1, j+dj1
                    if visit_count[i1][j1] == 1:
                        continue
                    # スコアが改善されれば更新
                    sc = cal_score(ANS_all[:t] + ANS_all[t+2:], all=True)
                    if sc < bestsc:
                        bestANS.pop(t)
                        bestANS.pop(t)
                        ANS_all.pop(t)
                        ANS_all.pop(t)
                        bestsc = sc
                        visit_count[i1][j1] -= 1
                        visit_count[i][j] -= 1
                        endflag = False
                        print("tempsc2:", t, Lcut, sc, file=sys.stderr)
                        continue
            ANS_all, bestsc = improve2(ANS_all, bestsc, time_keeper.time_now()+0.03)
        return ANS_all, bestsc

    def improve2(ANS_all, bestsc, T_LIMIT):
        # パス変更による改善
        # visit_time = cal_visit_time(ANS_all) #?????
        cnt = 0
        while True:
            cnt += 1
            if time_keeper.is_time_over(T_LIMIT):
                print("timeover:", file=sys.stderr)
                return ANS_all, bestsc

            t = random.randrange(len(ANS_all)-1)
            i, j, dir, c = ANS_all[t] # 現在地点
            i2, j2, dir2, c2 = ANS_all[t+1] # 次の地点
            # LLとかLRとかは却下
            if (dir + dir2) % 2 == 0:
                continue
            di, dj = to_dij[c] # 現在地点から次の地点への差分
            di2, dj2 = to_dij[c2] # 次の地点から到達地点への差分
            dir_, c_ = dir2, c2 # 現在地点の改善案
            di_, dj_ = to_dij[c2] # 現在地点から次の地点への差分
            i2_, j2_, dir2_, c2_ = i + di_, j + dj_, dir, c # 次の地点の改善案

            # 壁で移動できない場合は却下
            if dir_ not in movable[i][j] or dir2_ not in movable[i2_][j2_]:
                continue
            # 省略すると未到達セルが生じる場合も却下
            if visit_count[i2][j2] == 1:
                continue
            # スコアが改善されれば更新
            ANS_all[t] = (i, j, dir_, c_)
            ANS_all[t+1] = (i2_, j2_, dir2_, c2_)
            sc = cal_score(ANS_all, all=True)

            if sc < bestsc:
                print("tempsc_rev:", cnt, sc, file=sys.stderr)
                bestsc = sc
                visit_count[i2][j2] -= 1
                visit_count[i2_][j2_] += 1
                continue
            else:
                ANS_all[t] = (i, j, dir, c)
                ANS_all[t+1] = (i2, j2, dir2, c2)
        return ANS_all, bestsc

    def improve_add(ANS_all, bestsc, T_LIMIT):
        # パス追加による改善
        cnt = 0
        while True:
            cnt += 1
            if time_keeper.is_time_over(T_LIMIT):
                print("timeover:", file=sys.stderr)
                return ANS_all, bestsc

            t = random.randrange(len(ANS_all)-1)
            i, j, dir, c = ANS_all[t] # 現在地点
            i2, j2, dir2, c2 = ANS_all[t+1] # 次の地点
            PATH = []
            while True:
                ddi = random.randint(-2, 2)
                ddj = random.randint(-2, 2)
                ito, jto = i+ddi, j+ddj
                if 0<=ito<N and 0<=jto<N and (i, j) != (ito, jto):
                    break
            path = moveBFS(i, j, ito, jto)
            PATH.extend(path[:len(path)-1])
            path = moveBFS(ito, jto, i2, j2)
            PATH.extend(path[:len(path)])
            ANS = []
            for t_ in range(len(PATH)-1):
                ii, jj = PATH[t_]
                ii2, jj2 = PATH[t_+1]
                di, dj = ii2-ii, jj2-jj
                ANS.append(to_DIR[(di, dj)])
            ANS_all_ = []
            inow, jnow = i, j
            for c_ in ANS:
                di, dj = to_dij[c_]
                dir = to_dir[c_]
                ANS_all_.append((inow, jnow, dir, c_))
                inow += di
                jnow += dj
            # スコアが改善されれば更新
            sc = cal_score(ANS_all[:t] + ANS_all_ + ANS_all[t+1:], all=True)
            if sc < bestsc:
                ANS_all = ANS_all[:t] + ANS_all_ + ANS_all[t+1:]
                bestsc = sc
                for i, j, dir, c in ANS_all_:
                    visit_count[i][j] += 1
                visit_count[i2][j2] -= 1
                print("tempsc_add:", t, sc, file=sys.stderr)
                continue
        return ANS_all, bestsc


    ANS_all = []
    visit_count = [[0] * N for _ in range(N)]
    i, j = 0, 0
    for c in bestANS:
        di, dj = to_dij[c]
        dir = to_dir[c]
        ANS_all.append((i, j, dir, c))
        visit_count[i][j] += 1
        i += di
        j += dj

    bestsc0 = bestsc
    ANS_all, bestsc = improve(ANS_all, bestsc, LIMIT2)
    print(f"{bestsc0} to {bestsc} : improved {(bestsc / bestsc0):.2f}", file=sys.stderr)

    ANS_all, bestsc = improve_add(ANS_all, bestsc, LIMIT3)

    bestANS = []
    for i, j, dir, c in ANS_all:
        bestANS.append(c)
    # 出力
    bestsc = cal_score(bestANS)
    print("".join(bestANS))
    print("SC:", bestsc, file=sys.stderr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Debug mode')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    main(args.debug)
