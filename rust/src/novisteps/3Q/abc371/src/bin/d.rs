use proconio::input;

fn main() {
    input! {
        N: usize,
        XN: [i64; N],
        PN: [u64; N],
        Q: u64,
    }

    let mut _sum = vec![0; N + 1];
    for i in 1..=N {
        _sum[i] += _sum[i - 1] + PN[i - 1]
    }
    for q in 0..Q {
        input! {
            L: i64,
            R: i64
        }
        let l_i = match XN.binary_search(&L) {
            Ok(i) => i,
            Err(i) => i,
        };
        let r_i = match XN.binary_search(&(R + 1)) {
            Ok(i) => i,
            Err(i) => i,
        };
        println!("{}", _sum[r_i] - _sum[l_i])
    }
}
