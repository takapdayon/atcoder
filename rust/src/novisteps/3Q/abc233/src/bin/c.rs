use std::convert::TryInto;

use proconio::input;

fn dfs(val: u128, N: u128, X: u128, LN: &Vec<Vec<u128>>, index: usize) -> usize {
    if index == N.try_into().unwrap() {
        if val == X {
            return 1;
        } else {
            return 0;
        }
    }

    let mut _sum = 0;
    for to in 0..LN[index].len() {
        _sum += dfs(val * LN[index][to], N, X, LN, index + 1)
    }

    return _sum;
}

fn main() {
    input! {
        N: u128,
        X: u128,
    }
    let mut result = 0;
    let mut LN: Vec<Vec<u128>> = vec![];
    for i in 0..N {
        input! {
            L: u128,
            aL: [u128; L]
        }
        LN.push(aL);
    }

    for i in 0..LN[0].len() {
        result += dfs(LN[0][i], N, X, &LN, 1);
    }

    println!("{}", result)
}
