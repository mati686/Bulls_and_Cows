import random

separator = "-" * 50
guess_count = 0

def welcome():
    print(f"""Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}
Enter a number:
{separator}
""")


def generate_number(a: int, b: int, digits: int) -> int:
    while True:
        gen_number = random.randint(a, b)
        set_number = set(str(gen_number))
        if len(set_number) == digits:
            break
        else:
            continue
    return gen_number


def user_number() -> int:
    number = int(input(">>>>"))
    return number


def s_end(animal: str, count: int) -> str:
    if count == 1:
        return animal
    else:
        return animal + "s"


def counting_guesses():
    global guess_count
    guess_count += 1


def score(guesses: int) -> str:
    if guesses > 10:
        return "not so good..."
    elif guesses > 5:
        return "average."
    else:
        return "amazing!"