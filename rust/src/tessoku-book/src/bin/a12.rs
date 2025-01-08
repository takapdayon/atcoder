use proconio::input;

fn check(mid: &usize, AN: &Vec<usize>, K: &usize) -> bool {
    let mut count = 0;
    for a in AN {
        count += mid / a
    }
    return count >= *K;
}

fn main() {
    input! {
        N: usize,
        K: usize,
        AN: [usize; N],
    }
    let mut ok = 10_usize.pow(9);
    let mut ng = 0;
    while (ok).abs_diff(ng) > 1 {
        let mid = (ok + ng) / 2;
        if check(&mid, &AN, &K) {
            ok = mid
        } else {
            ng = mid
        }
    }
    println!("{}", ok)
}
