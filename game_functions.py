import other_functions


separator = "-" * 50


def comparison(number1: int, number2: int) -> bool:
    if number1 == number2:
        return True
    else:
        return False


def bulls_cows(num1: int, num2: int) -> dict:
    bulls_cows_dict = {"bull": 0, "cow": 0}
    for i, j in enumerate(str(num1)):
        if j in str(num2) and i == str(num2).index(j):
            bulls_cows_dict["bull"] += 1
        elif j in str(num2) and i != str(num2).index(j):
            bulls_cows_dict["cow"] += 1
    return bulls_cows_dict


def win():
    print(f"""Correct, you've guessed the right number
in {other_functions.guess_count} guesses.
That's {other_functions.score(other_functions.guess_count)}
{separator}
""")


def game(gen_number: int):
    while comparison(usr_number := other_functions.user_number(), gen_number) is False:
        animals_dict = bulls_cows(usr_number, gen_number)
        print(f"{animals_dict['bull']} {other_functions.s_end('bull', animals_dict['bull'])}, "
              f"{animals_dict['cow']} {other_functions.s_end('cow', animals_dict['cow'])}")
        print(separator)
        other_functions.counting_guesses()
    else:
        win()
