use std::collections::HashSet;

use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        N: usize,
        K: usize,
        AN: [isize; N]
    }

    let (before, after) = AN.split_at(N / 2);
    let mut be_sum: Vec<isize> = vec![];
    let mut af_set: HashSet<isize> = HashSet::new();

    for i in 0..=before.len() {
        for com in before.iter().combinations(i) {
            be_sum.push(com.iter().copied().sum())
        }
    }

    for i in 0..=after.len() {
        for com in after.iter().combinations(i) {
            af_set.insert(com.iter().copied().sum());
        }
    }

    for i in 0..be_sum.len() {
        if af_set.contains(&(K as isize - be_sum[i] as isize)) {
            println!("Yes");
            return;
        }
    }

    println!("No")
}
