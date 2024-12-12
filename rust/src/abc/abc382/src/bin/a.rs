use proconio::input;

fn main() {
    input! {
        N: usize,
        D: usize,
        S: String,
    }
    println!("{}", D + S.chars().filter(|s| *s == '.').count())
}
