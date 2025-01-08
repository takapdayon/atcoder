use proconio::input;

fn main() {
    input! {
        N: usize,
        PAN: [(usize, usize); N]
    }
    let mut dp = vec![vec![0; N + 1]; N + 1];
    for i in 1..=N {
        for j in (i..=N).rev() {
            if j != N {
                if i <= PAN[j].0 && PAN[j].0 <= j {
                    dp[i][j] = dp[i][j + 1] + PAN[j].1;
                } else {
                    dp[i][j] = dp[i][j + 1]
                }
            }
            if i != 1 {
                if i <= PAN[i - 2].0 && PAN[i - 2].0 <= j {
                    dp[i][j] = dp[i][j].max(dp[i - 1][j] + PAN[i - 2].1)
                } else {
                    dp[i][j] = dp[i][j].max(dp[i - 1][j])
                }
            }
        }
    }
    let mut result = 0;
    for i in 0..=N {
        result = result.max(dp[i][i])
    }
    println!("{}", result)
}
