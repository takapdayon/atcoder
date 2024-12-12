use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        N: usize,
        mut D: usize,
        mut S: Chars
    }
    for i in 0..N {
        if S[N - i - 1] == '@' && D != 0 {
            S[N - i - 1] = '.';
            D -= 1;
        }
    }
    println!("{}", S.iter().collect::<String>())
}
