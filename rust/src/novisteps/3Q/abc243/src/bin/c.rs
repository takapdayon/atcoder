use proconio::input;
use proconio::marker::Chars;
use std::collections::HashMap;

fn main() {
    input! {
        N: isize,
        XYN: [(isize, isize); N],
        S: Chars,
    }
    let mut memo: HashMap<(isize, char), isize> = HashMap::new();
    for (i, (x, y)) in XYN.iter().enumerate() {
        if S[i] == 'L' {
            if let Some(&r) = memo.get(&(*y, 'R')) {
                if r <= *x {
                    println!("Yes");
                    return;
                }
            }
            memo.entry((*y, 'L'))
                .and_modify(|val| *val = (*val).max(*x))
                .or_insert(*x);
        } else {
            if let Some(&l) = memo.get(&(*y, 'L')) {
                if l >= *x {
                    println!("Yes");
                    return;
                }
            }
            memo.entry((*y, 'R'))
                .and_modify(|val| *val = (*val).min(*x))
                .or_insert(*x);
        }
    }
    println!("No")
}
