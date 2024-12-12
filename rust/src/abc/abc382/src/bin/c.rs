use proconio::input;

fn main() {
    input! {
        N: usize,
        M: usize,
        AN: [usize; N],
        BM: [usize; M]
    }
    let mut _min = *BM.iter().max().unwrap_or(&0) + 1;
    let mut memo = vec![0; _min];
    for (i, &a) in AN.iter().enumerate() {
        if _min >= a {
            while _min >= a {
                memo[_min - 1] = i + 1;
                _min -= 1;
            }
        }
    }
    for &b in BM.iter() {
        if memo[b - 1] == 0 {
            println!("{}", -1)
        } else {
            println!("{}", memo[b - 1])
        }
    }
}
