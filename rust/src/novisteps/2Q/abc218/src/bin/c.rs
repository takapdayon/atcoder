use proconio::{input, marker::Chars};

fn rot(grid: &Vec<Vec<char>>) -> Vec<Vec<char>> {
    let n = grid.len();
    let mut c_grid = grid.clone();
    for h in 0..n {
        for w in 0..n {
            c_grid[h][w] = grid[n - w - 1][h];
        }
    }
    return c_grid;
}

fn main() {
    input! {
        N: usize,
        SN: [Chars; N],
        mut TN: [Chars; N]
    }
    let s_count = SN
        .iter()
        .flat_map(|h| h.iter())
        .filter(|&&w| w == '#')
        .count();

    let t_count = TN
        .iter()
        .flat_map(|h| h.iter())
        .filter(|&&w| w == '#')
        .count();

    if s_count != t_count {
        println!("No");
        return;
    }

    let mut s_vec: Vec<usize> = vec![];
    for h in 0..N {
        for w in 0..N {
            if SN[h][w] == '#' {
                s_vec.push(h * N + w)
            }
        }
    }

    // ここら辺の回転、どうやるのがいいのだ...本番できる気がしない
    for _ in 0..4 {
        let mut t_vec: Vec<usize> = vec![];
        for h in 0..N {
            for w in 0..N {
                if TN[h][w] == '#' {
                    t_vec.push(h * N + w)
                }
            }
        }

        let diff = (s_vec[0] as isize - t_vec[0] as isize);
        let mut flag = true;
        for i in 0..s_vec.len() {
            let s_v = s_vec[i] as isize;
            let t_v = t_vec[i] as isize;
            if (s_v - t_v) != diff {
                flag = false
            }
        }
        if flag {
            println!("Yes");
            return;
        }
        TN = rot(&TN);
    }
    println!("No")
}
