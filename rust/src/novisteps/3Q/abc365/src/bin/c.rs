use proconio::input;

fn solve(mid: i64, AN: &Vec<i64>, M: &i64) -> bool {
    let mut sum: i64 = 0;
    for a in AN.iter() {
        sum += a.min(&mid);
    }
    return sum <= *M;
}

fn main() {
    input! {
        N: i64,
        M: i64,
        AN: [i64; N]
    }

    if AN.iter().sum::<i64>() <= M {
        println!("infinite");
        return;
    }

    let mut ok: i64 = 0;
    let mut ng: i64 = 10_i64.pow(9);

    while (ok - ng).abs() > 1 {
        let mid = (ok + ng) / 2;
        if solve(mid, &AN, &M) {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    println!("{}", ok);
}
