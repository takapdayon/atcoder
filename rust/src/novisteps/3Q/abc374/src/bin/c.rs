use proconio::input;

fn main() {
    input! {
        N: usize,
        KN: [u64; N]
    }
    let sum: u64 = KN.iter().sum();
    let mut result = u64::MAX;
    for flag in 0..1 << N {
        let mut a = 0;
        for i in 0..N {
            if flag & (1 << i) != 0 {
                a += KN[i]
            }
        }
        result = result.min(a.max(sum - a));
    }
    println!("{}", result)
}
