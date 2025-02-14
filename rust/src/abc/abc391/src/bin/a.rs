use im_rc::{hashmap, HashMap};
use proconio::input;

fn main() {
    input! {
        D: String,
    }
    let directions: HashMap<&str, &str> = hashmap! {
        "N" => "S",
        "S" => "N",
        "W" => "E",
        "E" => "W",
        "NE" => "SW",
        "SW" => "NE",
        "NW" => "SE",
        "SE" => "NW",
    };
    println!("{}", directions.get(&D.as_str()).unwrap());
}
