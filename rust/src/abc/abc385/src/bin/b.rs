use proconio::{input, marker::Chars};

fn main() {
    input! {
        H: usize,
        W: usize,
        mut X: usize,
        mut Y: usize,
        SHW: [Chars; H],
        T: Chars
    }
    let mut grid = vec![vec![false; W]; H];
    for t in T.iter() {
        if *t == 'U' && X != 0 && SHW[X - 2][Y - 1] != '#' {
            X -= 1;
        } else if *t == 'D' && X != (H - 1) && SHW[X][Y - 1] != '#' {
            X += 1;
        } else if *t == 'L' && Y != 0 && SHW[X - 1][Y - 2] != '#' {
            Y -= 1;
        } else if *t == 'R' && Y != (W - 1) && SHW[X - 1][Y] != '#' {
            Y += 1;
        }
        if SHW[X - 1][Y - 1] == '@' {
            grid[X - 1][Y - 1] = true
        }
    }
    let count = grid.iter().flat_map(|h| h.iter()).filter(|&&w| w).count();

    println!("{} {} {}", X, Y, count)
}
