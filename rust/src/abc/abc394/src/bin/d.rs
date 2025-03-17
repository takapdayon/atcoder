use std::collections::VecDeque;

use proconio::{input, marker::Chars};

fn main() {
    input! {
        S: Chars
    }
    let mut af = vec![];
    let mut queue = VecDeque::from(S);
    while queue.len() != 0 {
        let mut val = queue.pop_front().unwrap();
        if af.len() != 0 && af.last().unwrap() == &'(' && val == ')' {
            af.pop();
            continue;
        }
        if af.len() != 0 && af.last().unwrap() == &'[' && val == ']' {
            af.pop();
            continue;
        }
        if af.len() != 0 && af.last().unwrap() == &'<' && val == '>' {
            af.pop();
            continue;
        }
        af.push(val);
    }
    if af.len() != 0 {
        print!("No");
    } else {
        print!("Yes");
    }
}
