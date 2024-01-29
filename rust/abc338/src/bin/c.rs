use proconio::input;
use proconio::marker::Chars;
use std::cmp::max;
use std::cmp::min;

fn main() {
    input! {
        n: usize,
        Q: [usize; n],
        A: [usize; n],
        B: [usize; n],
    }
    let mut result = 0;
    for i in 0..=Q.iter().max().unwrap() {
        let y = 10 * *9;
        for w in 0..n {
            if Q[w] < A[w] * i {
                y = (-10 * *9);
                continue;
            }
            if B[w] > 0 {
                y = min(y, ((Q[w] - A[w] * i) / B[w]).floor());
            }
        }
        result = max(result, i + y);
    }
    println!("{}", result);
}
