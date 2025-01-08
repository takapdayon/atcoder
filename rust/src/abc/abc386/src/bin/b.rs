use std::collections::VecDeque;

use proconio::input;

fn main() {
    input! {
        S: String
    }
    let mut s_queue: VecDeque<char> = S.chars().into_iter().collect();
    let mut result = 0;
    while !s_queue.is_empty() {
        let s = s_queue.pop_front().unwrap();
        if s == '0' && !s_queue.is_empty() && s_queue[0] == '0' {
            s_queue.pop_front();
        }
        result += 1;
    }
    println!("{}", result)
}
