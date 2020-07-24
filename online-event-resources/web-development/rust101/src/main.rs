use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    let number = rand::thread_rng().gen_range(1,11);
    println!("The number is: {}", number);

    loop {
        println!("Guess a number between 1 and 10: ");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        println!("You guessed: {}", guess);
        
        let guess: u32 = guess.trim().parse().expect("Please type a number");
        
        match guess.cmp(&number) {
            Ordering::Less => println!("Too low"),
            Ordering::Greater => println!("Too high"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
