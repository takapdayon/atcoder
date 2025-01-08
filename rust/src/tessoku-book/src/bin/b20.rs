use proconio::{input, marker::Chars};

fn main() {
    input! {
        S: Chars,
        T: Chars
    }
    let mut dp = vec![vec![0; T.len() + 1]; S.len() + 1];
    for s in 0..=S.len() {
        for t in 0..=T.len() {
            if s >= 1 && t >= 1 && S[s - 1] == T[t - 1] {
                dp[s][t] = (dp[s - 1][t] + 1)
                    .min(dp[s][t - 1] + 1)
                    .min(dp[s - 1][t - 1])
            } else if s >= 1 && t >= 1 {
                dp[s][t] = (dp[s - 1][t] + 1)
                    .min(dp[s][t - 1] + 1)
                    .min(dp[s - 1][t - 1] + 1)
            } else if s >= 1 {
                dp[s][t] = dp[s - 1][t] + 1
            } else if t >= 1 {
                dp[s][t] = dp[s][t - 1] + 1
            }
        }
    }
    println!("{}", dp[S.len()][T.len()])
}
