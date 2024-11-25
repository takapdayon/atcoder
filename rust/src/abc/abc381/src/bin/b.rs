use proconio::input;

fn main() {
    input! {
        S: String
    }
    let mut pre: Option<char> = None;

    for s in S.chars() {
        if S.matches(s).count() != 2 {
            println!("No");
            return;
        }

        if let Some(pre_c) = pre {
            if s != pre_c {
                println!("No");
                return;
            }
            pre = None;
        } else {
            pre = Some(s);
        }
    }

    println!("Yes")
}
