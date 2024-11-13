use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        b: usize,
        alist: [usize; n],
        clist: [usize; m],
    }
    let result: usize =
        b * n * m + alist.iter().sum::<usize>() * m + clist.iter().sum::<usize>() * n;
    println!("{}", result)
}
