fn high_and_low(numbers: &str) {
    use std::cmp;
    let f = |(max, min), x| (cmp::max(max, x), cmp::min(min, x));

    let answer = numbers.split_whitespace().map(|x| x.parse::<i32>().unwrap()).fold((i32::min_value(), i32::max_value()), f);
    format!("{} {}", answer.0, answer.1);
}

fn main() {
    print!(high_and_low("1 2 3 4 5"));
}
