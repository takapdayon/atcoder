use std::collections::{HashMap, HashSet};

use proconio::input;

fn main() {
    input! {
        N: usize,
        AN: [usize; N],
    }
    let mut memo: HashMap<usize, usize> = HashMap::new();
    let mut set_AN: HashSet<usize> = AN.iter().cloned().collect();
    let mut set: HashSet<usize> = HashSet::new();
    let mut result = set_AN.len();
    for a in AN.iter() {
        *memo.entry(*a).or_insert(0) += 1;
    }

    for a in AN.iter() {
        if let Some(m) = memo.get_mut(a) {
            *m -= 1;
            set.insert(*a);
            if *m == 0 {
                set_AN.remove(a);
            }
            result = result.max(set_AN.len() + set.len());
        }
    }
    println!("{}", result);
}
