use proconio::input;

fn main() {
    input! {
        N: usize,
        AN: [usize; N - 1],
        BN: [usize; N - 2]
    }
    let mut dp = vec![0; N];
    dp[1] = AN[0];
    for i in 2..(2 + BN.len()) {
        dp[i] = (dp[i - 1] + AN[i - 1]).min(dp[i - 2] + BN[i - 2])
    }
    println!("{}", dp[N - 1])
}
