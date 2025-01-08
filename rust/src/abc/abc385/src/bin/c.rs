use proconio::input;

fn main() {
    input! {
        N: usize,
        HN: [usize; N]
    }
    let mut result = 1;
    for h in 0..N {
        for case in 0..h {
            let mut last = 0;
            let mut count = 0;
            for w in HN[case..].iter().skip(h) {
                if *w == last {
                    count += 1;
                } else {
                    last = *w;
                    result = result.max(count);
                    count = 1;
                }
            }
            result = result.max(count);
        }
    }
    println!("{}", result)
}
