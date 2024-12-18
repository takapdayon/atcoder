use proconio::input;

fn main() {
    input! {
        S: usize,
    }
    let MOD = 10_usize.pow(9) + 7;
    let mut dp = vec![0; S + 1];

    dp[0] = 1;

    for i in 3..=S {
        let mut sum = 0;
        for pre in 0..=(i - 3) {
            sum += dp[pre];
        }
        dp[i] = sum % MOD;
    }

    println!("{}", dp[S])
}
