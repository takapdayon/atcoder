use proconio::input;

fn main() {
    input! {
        N: usize,
        ABCDN: [(usize, usize, usize, usize); N]
    }
    let mut c_sum = vec![vec![0; 1501]; 1501];
    for (a, b, c, d) in ABCDN {
        c_sum[a][b] += 1;
        c_sum[a][d] -= 1;
        c_sum[c][b] -= 1;
        c_sum[c][d] += 1;
    }
    for h in 0..=1500 {
        for w in 1..=1500 {
            c_sum[h][w] += c_sum[h][w - 1];
        }
    }
    for h in 1..=1500 {
        for w in 0..=1500 {
            c_sum[h][w] += c_sum[h - 1][w];
        }
    }

    let count = c_sum
        .iter()
        .flat_map(|x| x.iter())
        .filter(|&&x| x > 0)
        .count();
    println!("{}", count)
}
