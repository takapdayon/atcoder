use proconio::input;
use std::cmp::max;

fn main() {
    input! {
        n: usize,
        mut k: usize,
        abrows: [(usize, usize); n]
    }
    let mut c_sum = [[0usize; 101]; 101];
    k += 1;
    for (a, b) in abrows {
        c_sum[a][b] += 1;
        if b + k <= 100 {
            c_sum[a][b + k] -= 1;
        }
        if a + k <= 100 {
            c_sum[a + k][b] -= 1;
        }
        if a + k <= 100 && b + k <= 100 {
            c_sum[a + k][b + k] += 1;
        }
    }

    for h in 1..101 {
        for w in 1..101 {
            c_sum[h][w] += c_sum[h][w - 1];
        }
    }
    for w in 1..101 {
        for h in 1..101 {
            c_sum[h][w] += c_sum[h - 1][w];
        }
    }

    let mut result = 0;

    for h in 1..101 {
        for w in 1..101 {
            result = result.max(c_sum[h][w]);
        }
    }

    println!("{}", &result)
}
