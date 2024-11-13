use proconio::input;
use std::collections::{BinaryHeap, HashMap};

fn main() {
    input! {
        n: isize,
        d: isize,
        mut xyrows: [(isize, isize); n],
    };
    let mut heap = BinaryHeap::new();
    let mut hmap = HashMap::new();

    let mut result = 0;

    for (x, y) in xyrows {
        hmap.entry(x).or_insert(BinaryHeap::new()).push(-y);
    }

    for i in 1..=d {
        if let Some(entries) = hmap.get(&i) {
            for &entry in entries {
                heap.push(entry)
            }
        }
        if let Some(earn) = heap.pop() {
            result += -earn
        }
    }
}
