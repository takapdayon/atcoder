use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        N: usize,
        AN: [usize; N]
    }
    let mut result: usize = 0;
    let mut set: HashSet<usize> = HashSet::new();
    let mut left: usize = 1;

    for i in (0..N).step_by(2) {
        while left < N && AN[left] == AN[left - 1] && !set.contains(&AN[left]) {
            set.insert(AN[left]);
            left += 2
        }
        result = result.max(set.len());

        if left >= N {
            break;
        }
        if !AN[left] == AN[left - 1] {
            set.remove(&AN[i]);
        } else {
            set.clear()
        }
    }

    left = 2;
    set.clear();
    for i in (1..N).step_by(2) {
        while left < N && AN[left] == AN[left - 1] && !set.contains(&AN[left]) {
            set.insert(AN[left]);
            left += 2
        }
        result = result.max(set.len());

        if left >= N {
            break;
        }
        if !AN[left] == AN[left - 1] {
            set.remove(&AN[i]);
        } else {
            set.clear()
        }
    }

    println!("{}", result)
}
