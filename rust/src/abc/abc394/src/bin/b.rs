use proconio::input;

fn main() {
    input! {
        N: usize,
        mut SN: [String; N]
    }
    SN.sort_by_key(|c| c.len());
    println!("{}", SN.concat())
}
