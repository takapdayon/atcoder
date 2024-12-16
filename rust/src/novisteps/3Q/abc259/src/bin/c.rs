use proconio::{input, marker::Chars};
use std::collections::VecDeque;

fn main() {
    input! {
        S: Chars,
        T: Chars,
    }
    let mut prev_s = ' ';
    let mut prev_t = ' ';
    let mut queue_s = VecDeque::from(S);
    let mut queue_t = VecDeque::from(T);
    let mut flag = false;

    while !queue_t.is_empty() {
        let s = queue_s.pop_front().unwrap_or(' ');
        let mut t = queue_t.pop_front().unwrap_or(' ');

        if s == t {
            if prev_s == s {
                flag = true;
            } else {
                flag = false;
            }
            prev_s = s;
            prev_t = t;
            continue;
        }

        if prev_s == t && flag {
            while prev_t == t {
                t = queue_t.pop_front().unwrap_or(' ');
            }

            if s == t {
                prev_s = s;
                prev_t = t;
                continue;
            }
        }
        println!("No");
        return;
    }
    println!("Yes")
}
