use proconio::{input, marker::Chars};

fn check(M: &usize, h: usize, w: usize, SNN: &Vec<Vec<char>>, TMM: &Vec<Vec<char>>) -> bool {
    for hh in 0..*M {
        for ww in 0..*M {
            if SNN[hh + h][ww + w] != TMM[hh][ww] {
                return false;
            }
        }
    }
    return true;
}

fn main() {
    input! {
        N: usize,
        M: usize,
        SNN: [Chars; N],
        TMM: [Chars; M]
    }
    for h in 0..(N - M + 1) {
        for w in 0..(N - M + 1) {
            if SNN[h][w] != TMM[0][0] {
                continue;
            }
            if check(&M, h, w, &SNN, &TMM) {
                println!("{} {}", h + 1, w + 1)
            }
        }
    }
}
