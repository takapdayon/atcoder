use proconio::input;

fn main() {
    input! {
        A: usize,
        B: usize,
        C: usize
    }
    if A + B == C || A + C == B || B + C == A || (A == B && B == C) {
        println!("Yes")
    } else {
        println!("No")
    }
}
