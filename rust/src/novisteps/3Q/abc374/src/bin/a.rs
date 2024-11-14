use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        S: Chars
    }
    if S.ends_with(&['s', 'a', 'n']) {
        println!("Yes")
    } else {
        println!("No")
    }
}
