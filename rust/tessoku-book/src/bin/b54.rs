use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
    }
    let mut result = 0;
    let mut groups: HashMap<usize, i32> = HashMap::new();

    for _ in 0..n {
        input! {
            a: usize,
        }
        *groups.entry(a).or_insert(0) += 1;
    }
    for (_, &val) in groups.iter() {
        if val >= 2 {
            result += (val * (val - 1)) / 2;
        }
    }
    println!("{}", result);
}
