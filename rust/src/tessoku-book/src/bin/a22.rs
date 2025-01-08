use proconio::input;

fn main() {
    input! {
        N: usize,
        AN: [usize; N - 1],
        BN: [usize; N - 1],
    }
    let mut dp = vec![-15000; N];
    dp[0] = 0;

    for i in 0..(N - 1) {
        dp[AN[i] - 1] = dp[AN[i] - 1].max(dp[i] + 100);
        dp[BN[i] - 1] = dp[BN[i] - 1].max(dp[i] + 150);
    }
    println!("{}", dp[N - 1])
}
