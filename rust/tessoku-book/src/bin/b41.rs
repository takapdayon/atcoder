use proconio::input;

fn main() {
    input! {
        mut X: usize,
        mut Y: usize,
    }
    let mut results: Vec<(usize, usize)> = vec![];
    while X != 1 || Y != 1 {
        results.push((X, Y));
        if X > Y {
            X -= Y;
        } else {
            Y -= X;
        }
    }
    println!("{}", results.len());
    for (x, y) in results.iter().rev() {
        println!("{} {}", x, y)
    }
}
