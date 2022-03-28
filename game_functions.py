import other_functions

separator = "-" * 50


# porovnání jestli číslo stejné -> výhra nebo počet bulls and cows
def comparison(number1: int, number2: int) -> bool:
    if number1 == number2:
        return True
    else:
        return False


# porovnání zadaného čísla na počet bulls a cows
def bulls_cows(num1: int, num2: int) -> dict:
    bulls_cows_dict = {"bull": 0, "cow": 0}
    for i, j in enumerate(str(num1)):
        # BULLS - pokud je číslo v generovaném čísle a je i na stejné pozici
        if j in str(num2) and i == str(num2).index(j):
            bulls_cows_dict["bull"] += 1
        # COWS - pokud je číslo v generovaném čísle ale není na stejné pozici
        elif j in str(num2) and i != str(num2).index(j):
            bulls_cows_dict["cow"] += 1
    return bulls_cows_dict


# výhra - výpis, počet hádání, skóre
def win():
    print(f"""Correct, you've guessed the right number
in {other_functions.guess_count} guesses.
That's {other_functions.score(other_functions.guess_count)}
{separator}
""")


# HRA
def game(gen_number: int):
    # smyčka - pokud se zadané číslo nerovná generovanému
    while comparison(usr_number := other_functions.user_number(4), gen_number) is False:
        # porovnej Bulls a Cows na zdaném číslu a generovaném číslu
        animals_dict = bulls_cows(usr_number, gen_number)
        print(f"{animals_dict['bull']} {other_functions.s_end('bull', animals_dict['bull'])}, "
              f"{animals_dict['cow']} {other_functions.s_end('cow', animals_dict['cow'])}")
        print(separator)
        # počet hádání +1
        other_functions.counting_guesses()
    # pokdu se číla rovnají, tak je výhra
    else:
        other_functions.counting_guesses()
        win()
