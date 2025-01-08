use proconio::input;

fn main() {
    input! {
        N: usize,
        AN: [usize; N],
    }
    for i in 0..N {
        for j in 0..N {
            for k in 0..N {
                if i != j && j != k && i != k && AN[i] + AN[j] + AN[k] == 1000 {
                    println!("Yes");
                    return;
                }
            }
        }
    }
    println!("No")
}
