use std::collections::HashMap;

use proconio::input;

fn main() {
    input! {
        N: usize,
        K: i128,
        AN: [i128; N]
    }

    let mut result = 0;
    let mut c_sum: Vec<i128> = vec![0; N + 1];
    let mut c_sum_map: HashMap<i128, usize> = HashMap::new();

    for i in 1..=N {
        c_sum[i] = c_sum[i - 1] + AN[i - 1];
    }
    for c in &c_sum {
        result += c_sum_map.get(&(c - K)).unwrap_or(&0);

        let count = c_sum_map.entry(*c).or_insert(0);
        *count += 1;
    }

    println!("{}", result)
}
