use proconio::input;

fn main() {
    input! {
        N: usize,
        S: String
    }
    if S[..N / 2].matches('1').count() == N / 2
        && S.chars().nth(N / 2) == Some('/')
        && S[N / 2..].matches('2').count() == N / 2
    {
        println!("Yes")
    } else {
        println!("No")
    }
}
