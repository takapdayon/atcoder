use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        ss: Chars,
    }
    let mut stack = Vec::new();
    for (i, s) in ss.iter().enumerate() {
        if s == &'(' {
            stack.push(i + 1);
        } else {
            println!("{} {}", stack.pop().unwrap(), i + 1);
        }
    }
}
