use std::collections::VecDeque;

use proconio::{input, marker::Chars};

fn main() {
    input! {
        S: Chars
    }
    let mut queue = VecDeque::from(S);
    let mut result = vec![];
    while queue.len() != 0 {
        let val = queue.pop_front().unwrap();
        if result.len() != 0 && result.last().unwrap() == &'W' && val == 'A' {
            result.pop();
            let mut count = 1;
            while result.len() != 0 && result.last().unwrap() == &'W' {
                result.pop();
                count += 1;
            }
            result.push('A');
            for i in 0..count {
                result.push('C')
            }
        } else {
            result.push(val);
        }
    }
    println!("{}", result.into_iter().collect::<String>())
}
