use proconio::input;

fn main() {
    input! {
        N: usize,
        Q: usize,
        AN: [usize; N],
    }
    let mut c_sum = vec![0; N + 1];
    for i in 1..=N {
        c_sum[i] = c_sum[i - 1] + AN[i - 1]
    }
    for q in 0..Q {
        input! {
            L: usize,
            R: usize,
        }
        println!("{}", c_sum[R] - c_sum[L - 1])
    }
}
