use proconio::input;

fn main() {
    input! {
        mut S: String
    }
    S.retain(|c| c == '2');
    println!("{}", S)
}
