use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        k: usize,
        s: String,
    }

    if (s.matches("1").count() + k) % 2 == 1 {
        println!("No")
    } else {
        println!("Yes")
    }
}
