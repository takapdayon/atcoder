use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        c: String,
        _as: Chars,
    }
    let mut count = 0;

    for a in _as {
        if a == 'R' {
            count += 2;
        }
        if a == 'B' {
            count += 1;
        }
    }
    if count % 3 == 0 && c == "W" {
        println!("Yes");
    } else if count % 3 == 1 && c == "B" {
        println!("Yes");
    } else if count % 3 == 2 && c == "R" {
        println!("Yes");
    } else {
        println!("No");
    }
}
