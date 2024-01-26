use proconio::input;
use proconio::marker::Chars;
use std::cmp::max;

fn main() {
    input! {
        n: usize,
        s: Chars,
    }

    let mut grass = vec![1usize; n];
    for (i, &mozi) in s.iter().enumerate() {
        if mozi == 'A' {
            grass[i + 1] = grass[i] + 1
        }
    }
    for (i, &mozi) in s.iter().enumerate().rev() {
        if mozi == 'B' {
            grass[i] = max(grass[i + 1] + 1, grass[i])
        }
    }
    println!("{}", grass.iter().sum::<usize>());
}
