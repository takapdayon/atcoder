use proconio::input;

fn main() {
    input! {
        N: usize,
        T: isize,
        S: String,
        XN: [isize; N]
    }
    let mut result = 0;
    let mut left: Vec<isize> = vec![];
    let mut right: Vec<isize> = vec![];

    for (i, s) in S.chars().enumerate() {
        if s == '0' {
            left.push(XN[i]);
        } else {
            right.push(XN[i]);
        }
    }
    left.sort();
    right.sort();

    for &r in right.iter() {
        let mut bef = 0;
        match left.binary_search(&r) {
            Ok(index) => bef = index,
            Err(index) => bef = index,
        }
        let mut aft = 0;
        match left.binary_search(&(r + (T * 2))) {
            Ok(index) => aft = index + 1,
            Err(index) => aft = index,
        }
        result += aft - bef
    }
    println!("{}", result)
}
