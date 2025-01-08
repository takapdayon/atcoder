use proconio::input;

fn main() {
    input! {
        N: usize,
        XYN: [(usize, usize); N],
        Q: usize
    }
    let mut c_sum = vec![vec![0; 1501]; 1501];
    for (x, y) in XYN {
        c_sum[x][y] += 1;
    }

    for h in 1..=1500 {
        for w in 1..=1500 {
            c_sum[h][w] += c_sum[h][w - 1];
        }
    }
    for h in 1..=1500 {
        for w in 1..=1500 {
            c_sum[h][w] += c_sum[h - 1][w];
        }
    }

    for _ in 0..Q {
        input! {
            a: usize,
            b: usize,
            c: usize,
            d: usize
        }
        let result = c_sum[c][d] - c_sum[a - 1][d] - c_sum[c][b - 1] + c_sum[a - 1][b - 1];
        println!("{}", result)
    }
}
