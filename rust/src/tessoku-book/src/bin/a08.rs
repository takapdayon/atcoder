use proconio::input;

fn main() {
    input! {
        H: usize,
        W: usize,
        XHW: [[i64; W]; H],
        Q: usize
    }
    let mut c_sum = vec![vec![0; W + 1]; H + 1];
    for h in 1..=H {
        for w in 1..=W {
            c_sum[h][w] += c_sum[h][w - 1] + XHW[h - 1][w - 1]
        }
    }
    for h in 1..=H {
        for w in 1..=W {
            c_sum[h][w] += c_sum[h - 1][w]
        }
    }
    for q in 0..Q {
        input! {
            A: usize,
            B: usize,
            C: usize,
            D: usize
        }
        let result = c_sum[C][D] - c_sum[A - 1][D] - c_sum[C][B - 1] + c_sum[A - 1][B - 1];
        println!("{}", result)
    }
}
