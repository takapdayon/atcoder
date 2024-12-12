use proconio::input;

fn main() {
    input! {
        N: usize,
        M: usize,
        mut AN: [usize; N],
        mut BM: [usize; M]
    }
    let mut result = 0;
    AN.sort();
    BM.sort();
    BM.reverse();

    for &a in AN.iter() {
        let opt_last = BM.last();
        if let Some(&last) = opt_last {
            if last <= a {
                BM.pop();
                result += a;
            }
        }
    }
    if BM.is_empty() {
        println!("{}", result);
    } else {
        println!("-1");
    }
}
