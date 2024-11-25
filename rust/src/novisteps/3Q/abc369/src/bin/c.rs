use proconio::input;

fn main() {
    input! {
        N: isize,
        AN: [isize; N]
    }
    let mut result: isize = 0;

    if N == 1 {
        println!("1");
        return;
    }

    let mut diff: isize = AN[1] - AN[0];
    let mut pre: isize = AN[1];
    let mut count: isize = 2;

    for a in AN[2..].iter() {
        if a - pre == diff {
            count += 1;
        } else {
            result += (count * (count - 1)) / 2;
            count = 2;
            diff = a - pre;
        }
        pre = *a;
    }
    result += (count * (count - 1)) / 2;

    println!("{}", result + N)
}
