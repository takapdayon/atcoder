use proconio::input;

fn main() {
    input! {
        N: usize,
        mut AN: [usize; N],
        Q: usize,
    }
    AN.sort();
    for q in 0..Q {
        input! {
            X: usize,
        }
        let result = AN.partition_point(|val| val < &X);
        println!("{}", result)
    }
}
