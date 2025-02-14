use std::collections::HashMap;

use proconio::input;

fn main() {
    input! {
        N: usize,
    }
    let mut counts = vec![HashMap::new(); N];
    let mut KS = vec![];
    for i in 0..N {
        input! {
            K: usize,
            AK: [usize; K]
        }
        KS.push(K);
        for a in AK {
            counts[i].entry(a).and_modify(|val| *val += 1).or_insert(1);
        }
    }
    let mut result: f64 = 0.0;
    for i in 0..N {
        for j in (i + 1)..N {
            let mut count: i64 = 0;
            for (k, v) in &counts[i] {
                if let Some(&jv) = counts[j].get(&k) {
                    count += v * jv
                }
            }
            result = result.max(count as f64 / (KS[i] * KS[j]) as f64)
        }
    }

    println!("{}", result)
}
