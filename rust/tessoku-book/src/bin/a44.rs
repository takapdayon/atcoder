use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        n: usize,
        q: usize,
    }

    let mut an = (1..=n).collect::<Vec<usize>>();
    let mut is_r = false;

    for _ in 0..q {
        input! {
            i: usize,
        }

        if i == 2 {
            is_r = !is_r;
        }

        input! {
            x: usize,
        }
        let index = if is_r { n - x } else { x };

        if i == 3 {
            println!("{}", an[index])
        } else {
            input! {
                y: usize,
            }
            an[index] = y
        }
    }
}
