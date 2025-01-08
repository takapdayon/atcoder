use proconio::input;

fn main() {
    input! {
        N: usize,
        AN: [usize; N],
        Q: usize,
    }
    let mut w_c_sum = vec![0; N + 1];
    let mut l_c_sum = vec![0; N + 1];

    for i in 1..=N {
        w_c_sum[i] = w_c_sum[i - 1] + if AN[i - 1] == 1 { 1 } else { 0 };
        l_c_sum[i] = l_c_sum[i - 1] + if AN[i - 1] == 0 { 1 } else { 0 };
    }

    for q in 0..Q {
        input! {
            L: usize,
            R: usize,
        }
        let w_count = w_c_sum[R] - w_c_sum[L - 1];
        let l_count = l_c_sum[R] - l_c_sum[L - 1];
        if w_count == l_count {
            println!("draw")
        } else if w_count > l_count {
            println!("win")
        } else {
            println!("lose")
        }
    }
}
