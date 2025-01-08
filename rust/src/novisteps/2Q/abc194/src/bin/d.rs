use proconio::input;

fn main() {
    input! {
        N: usize,
    }
    let mut result: f64 = 0.0;
    for i in 1..N {
        result += N as f64 / i as f64
    }
    println!("{}", result)
}
