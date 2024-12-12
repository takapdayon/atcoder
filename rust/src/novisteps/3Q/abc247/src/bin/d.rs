use proconio::input;
use std::collections::VecDeque;

fn main() {
    input! {
        Q: usize,
    }
    let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
    for q in 0..Q {
        input! {
            query: u8
        }
        if query == 1 {
            input! {
                x: usize,
                mut c: usize
            }
            queue.push_back((x, c));
        } else {
            input! {
                mut c: usize,
            }
            let mut result = 0;
            while c != 0 {
                if let Some(mut val) = queue.pop_front() {
                    if val.1 > c {
                        val.1 -= c;
                        result += c * val.0;
                        c = 0;
                        queue.push_front(val);
                    } else {
                        c -= val.1;
                        result += val.0 * val.1
                    }
                }
            }
            println!("{}", result)
        }
    }
}
