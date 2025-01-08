use std::collections::VecDeque;

use proconio::{input, marker::Chars};

fn main() {
    input! {
        K: usize,
        S: Chars,
        T: Chars
    }
    if S.len().abs_diff(T.len()) > 1 {
        println!("No");
        return;
    }
    if S.len() == T.len() {
        let mut count = 0;
        let mut flag = false;
        while count != S.len() {
            if S[count] == T[count] {
                count += 1;
                continue;
            }
            if flag {
                println!("No");
                return;
            }
            flag = true;
            count += 1;
        }
        println!("Yes");
        return;
    }
    if S.len() > T.len() {
        let mut s_queue = VecDeque::from(S);
        let mut t_queue = VecDeque::from(T);
        let mut flag = false;
        let mut prev = ' ';
        while !s_queue.is_empty() {
            if t_queue.is_empty() {
                println!("Yes");
                return;
            }
            let s = s_queue.pop_front().unwrap();
            if prev == s {
                prev = ' ';
                continue;
            }
            let t = t_queue.pop_front().unwrap();
            if s == t {
                continue;
            }
            if flag {
                println!("No");
                return;
            }
            prev = t;
            flag = true;
        }
    } else {
        let mut s_queue = VecDeque::from(S);
        let mut t_queue = VecDeque::from(T);
        let mut flag = false;
        let mut prev = ' ';
        while !t_queue.is_empty() {
            if s_queue.is_empty() {
                println!("Yes");
                return;
            }
            let t = t_queue.pop_front().unwrap();
            if prev == t {
                prev = ' ';
                continue;
            }
            let s = s_queue.pop_front().unwrap();
            if s == t {
                continue;
            }
            if flag {
                println!("No");
                return;
            }
            prev = s;
            flag = true;
        }
    }
    println!("Yes")
}
