from rps import RockPaperScissors


def main():
    print('\n',('*'*12 + " Welcome to Rock, Paper, Scissors! " + '*'*12).center(100,' '), '\n')
    while True:
        try:
            print("Do you want to play with another player or with the computer?")
            print("Press 1 to play with another player.")
            print("Press 2 to play with the computer.")
            print('_'*22)
            choice = int(input("Enter your choice here: "))
            two_player = False
            computer_play = False
            rounds = int(input("Enter the number of rounds: "))
            print('_'*22)

            if choice == 1:
                two_player = True
            elif choice == 2:
                computer_play = True

            game = RockPaperScissors(two_players=two_player, play_with_computer=computer_play, rounds=rounds)
            game.play()

        except ValueError:
            print("Invalid input. Please enter a valid number of rounds.")
        except KeyboardInterrupt:
            print("Keyboard Interrupt pressed")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
