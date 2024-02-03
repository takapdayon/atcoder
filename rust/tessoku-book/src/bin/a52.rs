use proconio::input;
use std::collections::VecDeque;

fn main() {
    input! {
        q: usize,
    }
    let mut queue = VecDeque::new();

    for _ in 0..q {
        input! {
            i: usize,
        }
        if i == 1 {
            input! {
                name: String,
            }
            queue.push_back(name);
        }
        if i == 2 {
            println!("{}", queue[0]);
        }
        if i == 3 {
            queue.pop_front();
        }
    }
}
