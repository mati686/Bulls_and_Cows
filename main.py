import random


separator = "-" * 50
usr_number = 0
generated_number = 0
bulls_cows_dict = {"bull": 0, "cow": 0}


def welcome():
    print(f"""
Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}
Enter a number:
{separator}
""")


def generate_number():
    global generated_number
    while True:
        generated_number = random.randint(999, 10000)
        set_number = set(str(generated_number))
        if len(set_number) == 4:
            break
        else:
            continue


def user_number():
    global usr_number
    usr_number = int(input())
    return usr_number


def comparison():
    if user_number() == generated_number:
        return True
    else:
        bulls_cows()
        return False


def bulls_cows():
    global bulls_cows_dict
    bulls_cows_dict = {"bull": 0, "cow": 0}
    str_number = str(generated_number)
    for i, j in enumerate(str(usr_number)):
        if j in str_number and i == str_number.index(j):
            bulls_cows_dict["bull"] += 1
        elif j in str_number and i >= str_number.index(j):
            bulls_cows_dict["cow"] += 1


def s_end(animal: str):
    if bulls_cows_dict[animal] > 1:
        return animal + "s"
    else:
        return animal


def game():
    while comparison() is False:
        print(f"{bulls_cows_dict['bull']} {s_end('bull')}, {bulls_cows_dict['cow']} {s_end('cow')}")
        print(separator)
    else:
        print("Correct, you've guessed the right number")


def main():
    if __name__ == "__main__":
        welcome()
        generate_number()
        print(generated_number)
        game()


main()
