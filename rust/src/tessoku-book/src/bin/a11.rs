use proconio::input;

fn main() {
    input! {
        N: usize,
        X: usize,
        AN: [usize; N],
    }
    let result = match AN.binary_search(&X) {
        Ok(i) => i + 1,
        Err(i) => i + 1,
    };
    println!("{}", result)
}
