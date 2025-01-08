use proconio::input;

fn check(mid: &f64, N: &f64) -> bool {
    return (mid.powf(3.0) + mid) > *N;
}

fn main() {
    input! {
        N: f64
    }
    let mut ok = 10_f64.powf(9.0);
    let mut ng = 0.0;

    while (ok - ng).abs() > 0.0001 {
        let mid = (ok + ng) / 2.0;
        if check(&mid, &N) {
            ok = mid
        } else {
            ng = mid
        }
    }
    println!("{}", ok)
}
