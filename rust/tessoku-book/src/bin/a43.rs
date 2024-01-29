use proconio::input;
use std::cmp::max;

fn main() {
    input! {
        n: usize,
        l: usize,
        abrows: [(usize, String); n],
    }
    let mut result = 0;
    for (a, b) in abrows {
        if b == "E" {
            result = max(result, l - a)
        } else {
            result = max(result, a)
        }
    }
    println!("{}", result)
}
