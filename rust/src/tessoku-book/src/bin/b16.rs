use proconio::input;

fn main() {
    input! {
        N: usize,
        HN: [usize; N]
    }
    let mut dp = vec![0; N];
    dp[1] = HN[0];
    for i in 1..N {
        dp[i] = dp[i - 1] + (HN[i]).abs_diff(HN[i - 1]);
        if i != 1 {
            dp[i] = dp[i].min(dp[i - 2] + (HN[i]).abs_diff(HN[i - 2]))
        }
    }
    println!("{}", dp[N - 1])
}
