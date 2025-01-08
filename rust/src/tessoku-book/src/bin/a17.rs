use proconio::input;

fn main() {
    input! {
        N: usize,
        AN: [usize; N - 1],
        BN: [usize; N - 2],
    }
    let mut dp = vec![0; N];
    dp[1] = AN[0];
    for i in 2..N {
        dp[i] = (dp[i - 1] + AN[i - 1]).min(dp[i - 2] + BN[i - 2])
    }

    // 復元
    let mut results: Vec<usize> = vec![];
    let mut current = dp[N - 1];
    let mut cn = N - 1;
    results.push(cn);

    while current != 0 {
        if (dp[cn] - dp[cn - 1]) == AN[cn - 1] {
            cn -= 1;
            results.push(cn);
            current -= AN[cn]
        } else {
            cn -= 2;
            results.push(cn);
            current -= BN[cn];
        }
    }
    results.sort();

    println!("{}", results.len());
    for result in results {
        print!("{} ", result + 1)
    }
}
