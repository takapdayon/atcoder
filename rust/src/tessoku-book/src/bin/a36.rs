use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
    }
    if n * 2 - 2 > k {
        println!("No");
        return;
    }
    if k % 2 == 0 {
        println!("Yes");
    } else {
        println!("No");
    }
}
