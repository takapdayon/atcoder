use proconio::input;

fn main() {
    input! {
        N: usize,
        S: usize,
        AN: [usize; N],
    }
    let mut dp = vec![vec![false; S + 1]; N + 1];
    dp[0][0] = true;

    for h in 1..=N {
        for w in 0..=S {
            if AN[h] > w {
                return;
            }
            dp[h][w] = dp[h - 1][w] || dp[h - 1][w - AN[w]]
        }
    }
    if dp[N][S] {
        println!("Yes");
    } else {
        println!("No");
    }
}
