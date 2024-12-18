use proconio::input;

fn main() {
    input! {
        mut X: u128,
        Y: u128,
        A: u128,
        B: u128,
    }
    let mut result = 0;
    while X * A < X + B && X * A < Y {
        result += 1;
        X *= A;
    }
    if (Y - X) % B == 0 {
        result += (Y - X) / B - 1;
    } else {
        result += (Y - X) / B;
    }
    println!("{}", result)
}
