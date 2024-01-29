use proconio::input;

fn main() {
    input! {
        n: usize,
        alist: [usize; n]
    }
    let mut num = [0usize; 101];

    for a in alist {
        num[a % 100] += 1;
    }

    let mut result = 0;
    for i in 1..50 {
        result += num[i] * num[100 - i]
    }

    result += if num[0] > 0 {
        num[0] * (num[0] - 1) / 2
    } else {
        0
    };
    result += if num[50] > 0 {
        num[50] * (num[50] - 1) / 2
    } else {
        0
    };

    println!("{}", result)
}
