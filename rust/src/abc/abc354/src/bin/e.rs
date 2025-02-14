use proconio::input;

fn main() {
    input! {
        N: usize,
        ABN: [(usize, usize); N]
    }
    let mut dp = vec![false; 1 << N];

    for i in 0..(1 << N) {
        let mut flag = false;
        dp[i] = flag
    }
    if dp[1 << N] {
        println!("Takahashi")
    } else {
        println!("Aoki")
    }
}
