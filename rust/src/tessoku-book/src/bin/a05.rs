use proconio::input;

fn main() {
    input! {
        N: usize,
        K: usize
    }
    let mut count = 0;
    for i in 1..=N {
        for j in 1..=N {
            if i + j < K && K - (i + j) <= N {
                count += 1;
            }
        }
    }
    println!("{}", count)
}
