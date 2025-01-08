use proconio::input;

fn main() {
    input! {
        N: usize,
        X: usize,
        AN: [usize; N]
    }
    if AN.contains(&X) {
        println!("Yes")
    } else {
        println!("No")
    }
}
