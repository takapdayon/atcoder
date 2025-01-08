use proconio::input;

fn main() {
    input! {
        A: usize,
        B: usize
    }
    for i in A..=B {
        if 100 % i == 0 {
            println!("Yes");
            return;
        }
    }
    println!("No");
}
