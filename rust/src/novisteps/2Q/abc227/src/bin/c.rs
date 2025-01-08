use proconio::input;

fn main() {
    input! {
        N: u128,
    }
    let mut result: u128 = 0;
    for a in (1..).take_while(|&a| a * a * a <= N) {
        for b in (a..).take_while(|&b| a * b * b <= N) {
            result += N / (a * b) - b + 1
        }
    }
    println!("{}", result)
}
