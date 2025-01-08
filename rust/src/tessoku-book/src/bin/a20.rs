use proconio::{input, marker::Chars};

fn main() {
    input! {
        S: Chars,
        T: Chars,
    }
    let mut dp = vec![vec![0; T.len() + 1]; S.len() + 1];
    for s in 1..=S.len() {
        for t in 1..=T.len() {
            dp[s][t] = dp[s - 1][t].max(dp[s][t - 1]);
            if S[s - 1] == T[t - 1] {
                dp[s][t] = dp[s][t].max(dp[s - 1][t - 1] + 1);
            }
        }
    }
    println!("{}", dp[S.len()][T.len()])
}
