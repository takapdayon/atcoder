use proconio::input;
use std::cmp::max;

fn main() {
    input! {
        n: usize,
        abrows: [(isize, isize); n],
    }
    let mut pp = 0;
    let mut pm = 0;
    let mut mp = 0;
    let mut mm = 0;

    for (a, b) in abrows {
        if a + b > 0 {
            pp += a + b
        }
        if a - b > 0 {
            pm += a - b
        }
        if -a + b > 0 {
            mp += -a + b
        }
        if -a - b > 0 {
            mm += -a - b
        }
    }
    println!("{}", max(max(pp, pm), max(mp, mm)));
}
