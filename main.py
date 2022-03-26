import game_functions
import other_functions


def main():
    if __name__ == "__main__":
        other_functions.welcome()
        generated_number = other_functions.generate_number(999, 10000, 4)
        print(generated_number)
        game_functions.game(generated_number)


main()
