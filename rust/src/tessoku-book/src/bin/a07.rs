use proconio::input;

fn main() {
    input! {
        D: usize,
        N: usize,
    }
    let mut c_sum = vec![0; D + 1];
    for n in 0..N {
        input! {
            L: usize,
            R: usize,
        }
        c_sum[L - 1] += 1;
        c_sum[R] -= 1;
    }

    for i in 1..=D {
        c_sum[i] += c_sum[i - 1];
    }

    for i in 0..D {
        println!("{}", c_sum[i])
    }
}
