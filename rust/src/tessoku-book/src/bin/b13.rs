use proconio::input;

fn main() {
    input! {
        N: usize,
        K: usize,
        mut AN: [usize; N]
    }
    let mut price = 0;
    let mut result = 0;
    let mut left = 0;

    for right in 0..N {
        while left != N && AN[left] + price <= K {
            price += AN[left];
            left += 1;
            result += left - right;
        }
        price -= AN[right];
    }

    println!("{}", result)
}
