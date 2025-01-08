use proconio::input;

fn main() {
    input! {
        N: usize,
        W: usize,
        WVN: [(usize, usize); N]
    }
    let mut dp = vec![vec![10_usize.pow(19); 100001]; N + 1];
    dp[0][0] = 0;

    for n in 1..=N {
        for v in 0..=100000 {
            if WVN[n - 1].1 > v {
                dp[n][v] = dp[n - 1][v];
                continue;
            }
            dp[n][v] = dp[n - 1][v].min(dp[n - 1][v - WVN[n - 1].1] + WVN[n - 1].0)
        }
    }

    for v in (0..=100000).rev() {
        if dp[N][v] <= W {
            println!("{}", v);
            return;
        }
    }
}
