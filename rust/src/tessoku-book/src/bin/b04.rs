use proconio::input;

fn main() {
    input! {
        N: String,
    }
    let deci = u32::from_str_radix(&N, 2).unwrap_or(0);
    println!("{}", deci);
}
