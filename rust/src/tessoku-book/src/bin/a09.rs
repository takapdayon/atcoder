use proconio::input;

fn main() {
    input! {
        H: usize,
        W: usize,
        N: usize,
        ABCDN: [(usize, usize, usize, usize); N]
    }
    let mut c_sum = vec![vec![0; W + 2]; H + 2];
    for (a, b, c, d) in ABCDN {
        c_sum[a][b] += 1;
        c_sum[a][d + 1] -= 1;
        c_sum[c + 1][b] -= 1;
        c_sum[c + 1][d + 1] += 1;
    }

    for h in 1..=(H + 1) {
        for w in 1..=(W + 1) {
            c_sum[h][w] += c_sum[h][w - 1];
        }
    }
    for h in 1..=(H + 1) {
        for w in 1..=(W + 1) {
            c_sum[h][w] += c_sum[h - 1][w];
        }
    }

    for h in 1..=(H) {
        for w in 1..=(W) {
            print!("{} ", c_sum[h][w])
        }
        println!("");
    }
}
