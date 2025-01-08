use std::collections::HashSet;

use proconio::input;

fn main() {
    input! {
        N: u128,
        Q: u128,
        AN: [u128; N],
    }
    let mut ans: Vec<u128> = vec![];
    let set: HashSet<u128> = AN.into_iter().collect();
    for i in 1..(10u128.pow(5) * 2) {
        if !set.contains(&i) {
            ans.push(i);
        }
    }
    for q in 0..Q {
        input! {
            K: u128,
        }
        println!("{}", ans[(K - 1) as usize])
    }
}
