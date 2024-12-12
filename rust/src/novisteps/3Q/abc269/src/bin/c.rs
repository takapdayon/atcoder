use proconio::input;

fn main() {
    input! {
        N: usize
    }
    // bit全探索
    let b = format!("{:b}", N);
    for flag in 0..1 << b.len() {
        let mut result = vec![];
        for i in 0..b.len() {
            if flag & (1 << i) != 0 {
                result.push('1')
            } else {
                result.push('0')
            }
        }
        let to_string: String = result.into_iter().collect();
        println!("{:?}", usize::from_str_radix(to_string.as_str(), 2));
    }
}
