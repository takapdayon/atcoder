use std::collections::HashSet;

use proconio::input;

fn main() {
    input! {
        ABCD: [usize; 4]
    }
    let set: HashSet<_> = ABCD.iter().collect();
    if set.len() == 2 {
        println!("Yes");
        return;
    }
    println!("No")
}
