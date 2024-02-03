use proconio::input;

fn recursive(mut alist: Vec<char>, index: usize) {
    &alist[index - 1] = '@';
    if index - 2 == 0 {
        return;
    }
    if index + 1 > 0 {
        return;
    }
}

fn main() {
    input! {
        n: usize,
        x: usize,
        _as: String,
    }
    let mut list_a: Vec<char> = _as.chars().collect();
}
