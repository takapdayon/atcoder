use im_rc::HashMap;
use proconio::input;

fn main() {
    input! {
        N: usize,
        Q: usize,
    }
    let mut count = 0;
    let mut nests = vec![1; N + 1];
    let mut birds: HashMap<usize, usize> = HashMap::new();

    for n in 1..=N {
        birds.insert(n, n);
    }

    for q in 0..Q {
        input! {
            q1: usize,
        }
        if q1 == 1 {
            input! {
                P: usize,
                H: usize,
            }
            let prev_nest = birds.get(&P).unwrap();
            nests[*prev_nest] -= 1;
            if nests[*prev_nest] == 1 {
                count -= 1;
            }
            nests[H] += 1;
            if nests[H] == 2 {
                count += 1
            }
            birds.insert(P, H);
        } else {
            println!("{}", count)
        }
    }
}
