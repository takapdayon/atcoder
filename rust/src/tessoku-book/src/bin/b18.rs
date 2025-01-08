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

    if !dp[N][S] {
        println!("-1");
        return;
    }

    let mut results = vec![];
    let mut current = S;
    for n in (1..=N).rev() {
        if (current as isize - AN[n - 1] as isize >= 0) && dp[n][current - AN[n - 1]] {
            current -= AN[n - 1];
            results.push(n);
        }
    }

    results.sort();

    println!("{}", results.len());
    for result in results {
        print!("{} ", result)
    }
}
