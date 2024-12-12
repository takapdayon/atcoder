use proconio::input;

fn main() {
    input! {
        N: usize,
        M: usize,
        S: [String; N]
    }
    let mut result = 10_usize.pow(19);
    for flag in 0..1 << N {
        let mut mark = vec![false; M];
        let mut count = 0;
        for i in 0..N {
            if flag & (1 << i) != 0 {
                count += 1;
                for (m, s) in S[i].chars().enumerate() {
                    if s == 'o' {
                        mark[m] = true
                    }
                }
            }
            if mark.iter().all(|&m| m) {
                result = result.min(count);
            }
        }
    }

    println!("{}", result)
}
