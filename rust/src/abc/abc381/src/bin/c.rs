use proconio::input;

fn main() {
    input! {
        N: usize,
        S: String
    }
    let mut result = 0;
    let mut count_1 = 0;
    let mut count_2 = 0;

    let mut pre: Option<char> = None;

    for s in S.chars() {
        if pre != Some('1') && s == '1' {
            count_1 = 0;
        }
        if pre == Some('1') && s == '2' {
            count_1 = 0;
        }

        if s == '/' {
            count_2 = 0;
        }
        if s == '1' {
            count_1 += 1
        }
        if s == '2' {
            count_2 += 1;
            result = result.max(count_1.min(count_2));
        }
        pre = Some(s)
    }

    if result != 0 {
        println!("{}", result * 2 + 1)
    } else {
        if S.matches('/').count() != 0 {
            println!("1")
        } else {
            println!("0")
        }
    }
}
