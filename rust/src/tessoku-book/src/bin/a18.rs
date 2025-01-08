use proconio::input;

fn main() {
    input! {
        N: usize,
        S: usize,
        AN: [usize; N]
    }
    let mut dp = vec![vec![false; S + 1]; N + 1];

    dp[0][0] = true;

    for n in 1..=N {
        for s in 0..=S {
            if AN[n - 1] > s {
                dp[n][s] = dp[n - 1][s];
                continue;
            }
            dp[n][s] = dp[n - 1][s] || dp[n - 1][s - AN[n - 1]] || false
        }
    }

    if dp[N][S] {
        println!("Yes")
    } else {
        println!("No")
    }
}
