use proconio::input;

fn main() {
    input! {
        N: usize,
        K: usize,
        mut AN: [usize; N],
    }
    AN.sort();
    let mut count: i64 = 0;
    let mut result: i64 = 0;
    let mut left = 1;
    for right in 0..N {
        while left != N && (AN[left] - AN[right]) <= K {
            left += 1;
            count += 1;
            result += count;
        }
        count -= 1;
        if right == left {
            left += 1;
        }
    }
    println!("{}", result)
}
