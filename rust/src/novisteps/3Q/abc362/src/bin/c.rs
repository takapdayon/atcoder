use proconio::input;

fn main() {
    input! {
        N: usize,
        LRN: [(isize, isize); N]
    }
    let mut min_sum = 0;
    let mut max_sum = 0;
    for (l, r) in LRN.iter() {
        min_sum += l;
        max_sum += r
    }
    if min_sum > 0 || 0 > max_sum {
        println!("No");
        return;
    }
    let mut result: Vec<isize> = vec![];
    for (l, r) in LRN.iter() {
        let diff = (r - l).abs();
        if diff < max_sum {
            result.push(*l);
            max_sum -= diff
        } else {
            result.push(r - max_sum);
            max_sum = 0
        }
    }
    println!("Yes");
    println!(
        "{}",
        result
            .iter()
            .map(|x| x.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    )
}
