use proconio::input;

fn main() {
    input! {
        N: usize,
        HN: [isize; N]
    }
    let mut dp = vec![0; N];
    for i in 1..N {
        dp[i] = dp[i - 1] + (HN[i] - HN[i - 1]).abs();
        if i != 1 {
            dp[i] = dp[i].min(dp[i - 2] + (HN[i] - HN[i - 2]).abs())
        }
    }

    // 復元
    let mut results = vec![];
    let mut cn = N - 1;
    while cn != 0 {
        results.push(cn + 1);
        if dp[cn] == dp[cn - 1] + (HN[cn] - HN[cn - 1]).abs() {
            cn -= 1;
        } else {
            cn -= 2;
        }
    }
    results.push(1);
    results.sort();

    println!("{}", results.len());
    for result in results {
        print!("{} ", result)
    }
}
