use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        H: usize,
        W: usize,
        K: usize,
        cHW: [Chars; H]
    }
    let mut result = 0;
    for flag_h in 0..(1 << H) {
        for flag_w in 0..(1 << W) {
            let mut copy_cHW = cHW.clone();
            for i in 0..H {
                if flag_h & (1 << i) != 0 {
                    copy_cHW
                        .get_mut(i)
                        .map(|h| h.iter_mut().for_each(|x| *x = '.'));
                }
            }
            for i in 0..W {
                if flag_w & (1 << i) != 0 {
                    copy_cHW
                        .iter_mut()
                        .for_each(|h| *h.get_mut(i).unwrap() = '.');
                }
            }
            let count = copy_cHW
                .iter()
                .flat_map(|h| h.iter())
                .filter(|&&w| w == '#')
                .count();

            if count == K {
                result += 1;
            }
        }
    }
    println!("{}", result)
}
