use num::ToPrimitive;
use proconio::input;

fn main() {
    input! {
        N: usize,
        M: usize,
        ABM: [(usize, usize); M],
        K: usize,
        CDK: [(usize, usize); K]
    }
    let mut result = 0;

    for flag in 0..(1 << K) {
        let mut dishes = vec![false; N.to_usize().unwrap() + 1];
        for i in 0..K {
            if flag & (1 << i) != 0 {
                dishes[CDK[i].0] = true;
            } else {
                dishes[CDK[i].1] = true;
            }
        }

        let mut count = 0;
        for (a, b) in ABM.clone().into_iter() {
            if dishes[a] && dishes[b] {
                count += 1
            }
        }
        result = result.max(count)
    }

    println!("{}", result)
}
