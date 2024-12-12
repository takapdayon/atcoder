use proconio::input;
use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;

fn main() {
    input! {
        N: usize,
        K: usize,
        cN: [usize; N]
    }
    let mut counts: HashMap<usize, usize> = HashMap::new();
    let mut kinds: HashSet<usize> = HashSet::new();
    let mut queue: VecDeque<usize> = VecDeque::new();
    let mut result = 0;

    for (i, c) in cN.iter().enumerate() {
        kinds.insert(*c);
        counts.entry(*c).and_modify(|val| *val += 1).or_insert(1);
        queue.push_back(*c);
        if i >= K {
            let opt_od = queue.pop_front();
            if let Some(od) = opt_od {
                let val = counts.get_mut(&od).unwrap();
                *val -= 1;
                if *val == 0 {
                    kinds.remove(&od);
                }
            }
        }
        result = result.max(kinds.len());
    }

    println!("{}", result)
}
