use proconio::input;

fn main() {
    input! {
        N: usize
        K: usize
    }
    if (N * 2 - 2 > K) {
        println!('No')
    }
    if (K % 2 == 0) {
        println!('Yes')
    } else {
        println!('No')
    }
}
