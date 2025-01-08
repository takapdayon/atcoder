use std::collections::{BTreeSet, HashMap};

use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        N: usize,
        AN: [usize; N]
    }
    let mut memo: HashMap<usize, usize> = HashMap::new();
    let mut set: BTreeSet<usize> = BTreeSet::new();

    for &a in &AN {
        set.insert(a);
    }

    for (i, &value) in set.iter().enumerate() {
        memo.insert(value, i + 1);
    }

    for a in AN {
        print!("{} ", memo.get(&a).unwrap())
    }
}
