use proconio::input;

pub fn factorial(num: usize) -> usize {
    (1..=num).product()
}

fn main() {
    input! {
        n: usize,
        alist: [usize; n],
    }

    let mut group = [0usize; 101];
    let mut result = 0;

    for a in alist {
        group[a] += 1
    }

    for g in group {
        if g >= 3 {
            result += factorial(g) / (factorial(g - 3) * factorial(g - (g - 3)))
        }
    }
    println!("{}", result)
}
