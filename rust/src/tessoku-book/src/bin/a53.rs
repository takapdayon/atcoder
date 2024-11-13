use proconio::input;
use std::collections::BinaryHeap;

fn main() {
    input! {
        qsize: usize,
    };
    let mut q = BinaryHeap::new();
    for _ in 0..qsize {
        input! {
            h: usize
        }
        if h == 1 {
            input! {
                price: isize,
            }
            q.push(-price)
        }
        if h == 2 {
            println!("{}", -(*q.peek().unwrap()));
        }
        if h == 3 {
            q.pop().unwrap();
        }
    }
}
