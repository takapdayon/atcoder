use proconio::input;

fn main() {
    input! {
        q: usize,
    }
    let mut books = Vec::new();

    for _ in 0..q {
        input! {
            c: usize,
        }
        if c == 1 {
            input! {
                book: String,
            }
            books.push(book);
        }
        if c == 2 {
            println!("{}", books.last().unwrap());
        }
        if c == 3 {
            books.pop();
        }
    }
}
