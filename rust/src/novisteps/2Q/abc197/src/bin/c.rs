use proconio::input;

fn main() {
    input! {
        N: usize,
        AN: [usize; N]
    }
    let mut result = 10_usize.pow(19);
    for flag in 0..(1 << (N - 1)) {
        let mut stack: Vec<usize> = vec![];
        let mut memo = AN[0];
        for i in 0..(N - 1) {
            if flag & (1 << i) != 0 {
                stack.push(memo);
                memo = AN[i + 1];
            } else {
                memo = memo | AN[i + 1];
            }
        }
        if memo != 0 {
            stack.push(memo);
        }
        let mut ans = 0;
        for s in stack.into_iter() {
            ans = ans ^ s
        }
        result = result.min(ans);
    }
    println!("{}", result)
}
