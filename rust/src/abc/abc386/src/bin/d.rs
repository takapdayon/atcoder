use proconio::input;

fn main() {
    input! {
        N: usize,
        M: usize,
        mut XYC: [(usize, usize, char); M],
    }
    XYC.sort();
    let mut white = N + 1;
    for (x, y, c) in XYC {
        if c == 'W' {
            white = white.min(y)
        } else {
            if white <= y {
                println!("No");
                return;
            }
        }
    }
    println!("Yes")
}
