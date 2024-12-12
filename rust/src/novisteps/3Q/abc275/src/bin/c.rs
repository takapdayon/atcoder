use itertools::iproduct;
use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        grid: [Chars; 9]
    }
    let mut result = 0;

    for (h, w, sh, sw) in iproduct!(0..9, 0..9, 0..9, 0..9) {
        if grid[h][w] == '.' || grid[sh][sw] == '.' {
            continue;
        }
        let dh = sh - h;
        let dw = sw - w;
        let ih = sh + dw;
        let iw = sw + dw;
        let jh = ih + dh;
        let jw = iw + dw;
        if 0 <= ih
            && ih <= 8
            && 0 <= iw
            && iw <= 8
            && 0 <= jh
            && ih <= 8
            && 0 <= jw
            && jw <= 8
            && grid[ih][iw] == '#'
            && grid[jh][jw] == '#'
        {
            result += 1;
        }
    }

    println!("{}", result / 4)
}
