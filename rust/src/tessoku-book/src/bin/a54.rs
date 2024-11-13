use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        q: usize,
    }
    let mut score: HashMap<String, usize> = HashMap::new();
    for _ in 0..q {
        input! {
            h: usize,
            name: String,
        }
        if h == 1 {
            input! {
                s: usize,
            }
            score.insert(name, s);
        } else {
            println!("{}", score[&name])
        }
    }
}
