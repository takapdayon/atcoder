use proconio::input;

fn main() {
    input! {
        N: usize,
        AN: [usize; N],
        D: usize,
    }
    let AN_rev: Vec<usize> = AN.iter().rev().cloned().collect();

    let mut c_sum = vec![0; N + 1];
    let mut c_sum_rev = vec![0; N + 1];
    for i in 1..=N {
        c_sum[i] = c_sum[i - 1].max(AN[i - 1]);
        c_sum_rev[i] = c_sum_rev[i - 1].max(AN_rev[i - 1]);
    }
    for d in 0..D {
        input! {
            L: usize,
            R: usize,
        }
        let result = c_sum[L - 1].max(c_sum_rev[N - R]);
        println!("{}", result)
    }
}
