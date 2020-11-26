use std::io;
use rand::Rng;
use std::cmp::Ordering;

#[derive(Debug)]
struct Guesser {
    answer: u32
}

impl Guesser {
    fn make_guess(&self) -> std::cmp::Ordering {
        println!("Guess a number between 1 and 10: ");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        println!("You guessed: {}", guess);

        let guess: u32 = guess.trim().parse().expect("Please type a number");

        guess.cmp(&self.answer)
    }
}

fn main() {
    let number = rand::thread_rng().gen_range(1,11);
    println!("The number is: {}", number);

    let guesser = Guesser { answer: number };

    loop {
        match guesser.make_guess() {
            Ordering::Less => println!("Too low"),
            Ordering::Greater => println!("Too high"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
