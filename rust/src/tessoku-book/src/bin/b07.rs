use proconio::input;

fn main() {
    input! {
        T: usize,
        N: usize,
    }
    let mut c_sum = vec![0; T + 1];
    for n in 0..N {
        input! {
            L: usize,
            R: usize,
        }
        c_sum[L] += 1;
        c_sum[R] -= 1;
    }
    for i in 1..=T {
        c_sum[i] += c_sum[i - 1];
    }
    for t in 0..T {
        println!("{}", c_sum[t])
    }
}
