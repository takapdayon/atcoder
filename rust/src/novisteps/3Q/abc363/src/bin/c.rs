use itertools::Itertools;
use proconio::input;
use std::collections::HashSet;

fn check(case: &Vec<char>, K: &usize) -> bool {
    // Kの回文を含んでいるか判定
    let mut result = false;
    for i in 0..(case.len() - K + 1) {
        if case[i..i + K].iter().collect::<Vec<_>>()
            == case[i..i + K].iter().rev().collect::<Vec<_>>()
        {
            result = true;
            return result;
        }
    }

    return result;
}

fn main() {
    input! {
        N: usize,
        K: usize,
        S: String
    }
    let mut result: i32 = 0;

    for case in S
        .chars()
        .permutations(N)
        .collect::<HashSet<_>>()
        .into_iter()
        .collect::<Vec<_>>()
    {
        if check(&case, &K) {
            continue;
        }
        result += 1;
    }

    println!("{}", result)
}
