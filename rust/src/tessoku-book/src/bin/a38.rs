use proconio::input;
use std::cmp;

fn main() {
    input! {
        d: usize,
        n: usize,
        lrh: [(usize, usize, usize); n]
    }

    let mut days = vec![24usize; (d + 1)];

    for (l, r, h) in lrh {
        for day in l..=r {
            days[day] = cmp::min(days[day], h)
        }
    }
    println!("{}", days.iter().sum::<usize>() - 24)
}
