use proconio::input;

fn main() {
    input! {
        N: usize
    }
    let mut results: Vec<usize> = vec![0];
    for i in 0..60 {
        if N & (1 << i) != 0 {
            for r in 0..results.len() {
                results.push(results[r] | (1 << i))
            }
        }
    }

    for r in results {
        println!("{}", r)
    }
}
