use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        alist: [usize; m],
    }
    let mut answers = vec![m; n];
    for a in alist {
        answers[a - 1] -= 1;
    }
    for answer in answers {
        println!("{}", answer)
    }
}
