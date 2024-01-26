use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        n: usize,
        mut lrrows: [(usize, usize); n]
    }
    lrrows.sort_by(|(_, a), (_, b)| a.cmp(b));
    let mut result = 0;
    let mut current = 0;
    for (l, r) in lrrows {
        if l < current {
            continue;
        }
        result += 1;
        current = r;
    }
    println!("{}", result)
}
