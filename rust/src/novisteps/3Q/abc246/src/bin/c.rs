use std::convert::TryInto;

use proconio::input;

fn main() {
    input! {
        N: usize,
        K: usize,
        X: usize,
        AN: [usize; N]
    }
    let mut result = AN.iter().sum::<usize>();
    let mut count: usize = 0;
    let mut remain: Vec<usize> = vec![];

    for a in AN.into_iter() {
        let c = (a / X).min(K - count);
        result -= c * X;
        count += c;
        remain.push(a % X);
    }
    remain.sort();
    remain.reverse();

    for i in 0..remain.len().min(K - count) {
        result -= remain[i];
    }

    println!("{}", result)
}
