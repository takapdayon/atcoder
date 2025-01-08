use std::collections::HashMap;

use proconio::input;

fn main() {
    input! {
        N: usize,
        K: isize,
        AN: [isize; N],
        BN: [isize; N],
        CN: [isize; N],
        DN: [isize; N],
    }
    let mut ab: Vec<isize> = vec![];
    let mut cd: Vec<isize> = vec![];
    for i in 0..N {
        for j in 0..N {
            ab.push(AN[i] + BN[j]);
        }
    }
    for i in 0..N {
        for j in 0..N {
            cd.push(CN[i] + DN[j]);
        }
    }
    let mut memo: HashMap<isize, bool> = HashMap::new();
    for i in cd {
        memo.insert(i, true);
    }
    for i in ab {
        if let Some(&val) = memo.get(&(K - i)) {
            if val {
                println!("Yes");
                return;
            }
        }
    }
    println!("No")
}
