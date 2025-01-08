use proconio::input;

fn main() {
    input! {
        N: usize,
        W: usize,
        WVN: [(usize, usize); N]
    }
    let mut dp = vec![vec![0; W + 1]; N + 1];

    for n in 1..=N {
        for w in 0..=W {
            if WVN[n - 1].0 > w {
                dp[n][w] = dp[n - 1][w];
                continue;
            }
            dp[n][w] = dp[n - 1][w].max(dp[n - 1][w - WVN[n - 1].0] + WVN[n - 1].1)
        }
    }
    println!("{}", dp[N][W])
}
