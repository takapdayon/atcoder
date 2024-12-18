use proconio::input;

fn main() {
    input! {
        N: usize,
        ABN: [(usize, usize); N]
    }
    let mut sum_AB = vec![0; N];
    let mut sum_a = 0;
    let mut sum_b = 0;
    for (i, (a, b)) in ABN.iter().enumerate() {
        sum_AB[i] = *a * 2 + *b;
        sum_a += *a;
    }
    sum_AB.sort();
    sum_AB.reverse();

    for i in 0..sum_AB.len() {
        if sum_b + sum_AB[i] > sum_a {
            println!("{}", i + 1);
            return;
        }
        sum_b += sum_AB[i]
    }
}
