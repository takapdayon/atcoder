use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        S: String
    }

    let mut container: HashSet<char> = HashSet::new();
    let mut memo: Vec<Vec<char>> = vec![];

    for s in S.chars() {
        if s == '(' {
            memo.push(vec![])
        } else if s == ')' {
            let opt_con = memo.pop();
            if let Some(con) = opt_con {
                for con_s in con {
                    container.remove(&con_s);
                }
            }
        } else {
            if container.contains(&s) {
                println!("No");
                return;
            }
            container.insert(s);
            let opt_con = memo.pop();
            if let Some(mut con) = opt_con {
                con.push(s);
                memo.push(con);
            }
        }
    }

    println!("Yes");
}
