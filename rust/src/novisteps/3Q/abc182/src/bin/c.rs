use proconio::{input, marker::Chars};

fn main() {
    input! {
        N: Chars,
    }

    let mut result = 10_usize.pow(19);

    for flag in 0..(1 << N.len()) {
        let mut str: Vec<char> = vec![];
        for i in 0..N.len() {
            if flag & (1 << i) != 0 {
                str.insert(0, N[i]);
            }
        }
        let val = str.iter().collect::<String>().parse::<usize>().unwrap_or(0);
        if val != 0 && val % 3 == 0 {
            result = result.min(N.len() - str.len())
        }
    }
    if result == 10_usize.pow(19) {
        println!("{}", -1)
    } else {
        println!("{}", result)
    }
}
