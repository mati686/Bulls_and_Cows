import random

separator = "-" * 50
guess_count = 0


# uvítací hláška
def welcome():
    print(f"""Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}
Enter a number:
{separator}
""")


# generátor náhodného čísla a: OD, B: DO, digits: počet míst
def generate_number(a: int, b: int, digits: int) -> int:
    while True:
        gen_number = random.randint(a, b)
        set_number = set(str(gen_number))
        if len(set_number) == digits:
            break
        else:
            continue
    return gen_number


# vložení hadaného čísla uživatelem, argument - počet míst
def user_number(digits: int) -> int:
    error = "Zadej pouze 4 místné číslo, jednotlivá čísla se nesmí opakovat."
    # smyčka dokud nezadá Xmístné číslo bez opakujícíseho čísla
    while True:
        try:
            number = int(input(">>>>"))
            set_number = set(str(number))
            # kontrola jestli je správná délka a jestli se čísla neopakují pomocé SET
            if len(str(number)) != digits or len(set_number) != digits:
                print(error)
                continue
            else:
                return number
        except:
            print(error)
            continue


# zjištění monžného čísla cow/cows bull/bulls
def s_end(animal: str, count: int) -> str:
    if count == 1:
        return animal
    else:
        return animal + "s"


# počet hádání
def counting_guesses():
    global guess_count
    guess_count += 1


# skóre podle poečtu hádání
def score(guesses: int) -> str:
    if guesses > 10:
        return "not so good..."
    elif guesses > 5:
        return "average."
    else:
        return "amazing!"
