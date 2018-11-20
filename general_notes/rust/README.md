2018-11-07 Conferenza sul rust

What is Rust?
a) Rust is a programming language for writing and maintaining fast, reliable, and small-footprint code.
b) Rust is a systems programming language that runs blazingly fast, prevents segfaults, and guarantees thread safety.
c) Rust is a modern programming language that provides zero-cost abstractions to write correct and fast code.

History
Rust was firstly designed by Graydon Hoare in 2006 as a personal project.
Mozilla supports and open sources the project in 2009-2010.
In 2015 Rust reaches version 1.0!
Sometimes in December later this year Rust edition 2018 will be released!

Who's using Rust
firefox-logo dropbox-logo sentry-logo
npm-logo cloudflare-logo

Features
 - Compiled
 - Fast
 - Modern static type system
 - Safe manual memory management without garbage collection

Where to use Rust
 - Embedded
 - CLI
 - WebAssembly
 - Backend

Why use Rust
 - Hack without fear! (base phylosophy)

Why not to use Rust
 - Slow at compyling 
 - Low libraries

First code
fn main() {
    println!("Hello, world!");

    let question = "what's the answer to life, the universe and everything?";
    let answer = 42;
    println!("{} {}", question, answer);
}

il ! indica una macro, le macro sono più sicure del C/C++
in rust ci sono variabili mutabili tramite la direttiva mut
int mut a = 1;

esempio di fibonacci
fn fib(n: u64) -> u64 {
    let mut a = 1;
    let mut b = 0;

    for _ in 0..n {
        let tmp = a + b;

        b = a;
        a = tmp;
    }

    a
}
"a" fa il return della variabile

in rust non c'è il sistema di fare inheritance
e non sarà previsto in futuro 

impl User {
    fn new(name: String, age: u64) -> Self {
        User { name, age }
    }

    fn is_adult(&self) -> bool {
        self.age >= 18
    }
}

fn main() {
    let user = User::new("Daniele", 22);
    println!("{} is adult? {}", user.name, user.is_adult());
}

impl indica un gruppo di funzioni (implementation)
new è una funzione statica che ritorna un oggetto, è una convenzione
Self è un alias per dire User

Gestione delle tuple
fn main() {
    let point = (0, 0);
    println!("x: {} y: {}", point.0, point.1);

    let (x, y) = point;
    println!("x: {} y: {}", x, y);
}
gli interi sono int32
in generale non c'è bisogno, tranne in casi di ambiguità, di specificare il tipo

enum
enum Event {
    Quit,
    KeyPress(char),
    Click(u64, u64),
}

fn main() {
    inspect(Event::KeyPress('q'));
    inspect(Event::Click(42, 73));
    inspect(Event::Quit);
}

fn inspect(ev: Event) {
    match ev {
        Event::Quit => println!("Quitting"),
        Event::KeyPress(ch) => println!("Key pressed {}", ch),
        Event::Click(x, y) => println!("Click x: {} y: {}", x, y),
    }
}

le variabili all'interno delle parentesi negli elementi dell'enum si chiamano payload 
quando hai un quit scrive e basta
quando hai un keypress lo stampi
quando hai un click stampi le coordinate
le enum sono usate tantissimo
match sta per pattern matching
rust nn ha eccezioni
il numero di variabili deve essere nota a compile time
tutte le procedure devono ritornare un tipo coerente
Rust non ha overloading


Pattern Matching
fn is_quit_event(ev: Event) -> bool {
    match ev {
        Event::KeyPress('q') | Event::Quit => true,
        _ => false
    }
}

fn is_logo_click_event(ev: Event) -> bool {
    match ev {
        Event::Click(x, y) if x < 200 && y < 200 => true,
        _ => false
    }
}
Il pattern mathing deve essere asaustivo e fare tutte le versioni

Ownership
Each value in Rust has a variable that is called its owner.
There can only be one owner at a time.
When the owner goes out of scope, the value will be dropped.
fn main() {
    // v is the *owner* of the vector
    let v = vec![2, 42, 73, 1, 20];

    if v.is_empty() {
        println!("vec is empty!");
    } else {
        println!("{:?}", v);
    }

    // v is dropped here and the memory is deallocated
}
v è l'unica variabile che punta alla memoria di quel valore

Moving ownership
fn main() {
    let v = vec![1, 2, 3, 4, 5];

    // transfer ownership of v to reversed
    let rev = reversed(v);

    println!("reversed vec {:?}", rev);

    // doesn't compile because the ownership of v was
    // *moved* to reversed
    // println!("original {:?}", v);

    // rev goes out of scope and memory is released
}

fn reversed(mut v: Vec<u8>) -> Vec<u8> {
    v.reverse();

    // returning a variable means passing the
    // ownership back to the caller
    v
}
In questo caso reversed acquisisce l'onership del vettore in chiamata
e ritorna la stessa onership a rev
la macro vect! alloca un vettore
gli array sono sullo stack mentre i vect sono sull'heap
il problema è che non hai un passaggio per valore

Borrowing
fn main() {
    let v = vec![2, 42, 73, 1, 20];

    println!(
        "is first element 0? {}",
        is_first_elem_0(&v) // &v borrows v
    );

    // we can access v here because its
    // ownership wasn't moved
    println!("{:?}", v);

    // v is dropped here as usual
}

fn is_first_elem_0(v: &Vec<u8>) -> bool {
    if v.is_empty() {
        return false;
    }

    v[0] == 0
}
In questo caso si ha un prestito dell'onership

Mutable references
  is_first_elem_0(&mut v) // &v borrows v
  fn is_first_elem_0(v: &mut Vec<u8>) -> bool {

Rules for the borrow checker
 - Any reference must last for a scope no greater than that of owner
 - You can have one or more immutable references to a resource or exactly one mutable reference
   ( previene completamente la race condition )

Esempio che schianta
fn main() {
    let y: &i32;

    {
        let x = 5;
        y = &x;
    }

    println!("{}", y);
}

spostando let x = 5; a prima riga funziona
alla terza non funziona


fn main() {
    let mut v = vec![1, 2, 3];

    for i in &v {
        println!("{}", i);

        v.push(34);
    }
}
questo codice fatto in C++ era lo sclero perchè riallocavi il vettore
da tutt'altra parte e accedevi ad un altra
Rust lo impedisce

facendo 
for i in &mut v {
non risulta cmq valido perchè c'è v.push(34);


fn get_magic(id: &i64) -> &u8 {
    let magic = 42;

    if *id == 0 {
        &magic
    } else {
        &0
    }
}
Quando ritorna al chiamante lo scope della variabile muore e si ferma

INSTALL RUST
$ curl https://sh.rustup.rs -sSf | sh
$ rustup install stable
$ rustc --version

Compile
$ rustc main.rs && ./main

Create compile and run a project
$ cargo new exercises
$ cargo build
$ # main is src/main.rs
$ cargo run

Formatter - https://github.com/rust-lang-nursery/rustfmt
Linter - https://github.com/rust-lang-nursery/rust-clippy

