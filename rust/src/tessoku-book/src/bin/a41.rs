use proconio::input;

fn main() {
    input! {
        n: usize,
        s: String,
    };
    if s.contains("BBB") || s.contains("RRR") {
        println!("Yes");
    } else {
        println!("No")
    }
}
