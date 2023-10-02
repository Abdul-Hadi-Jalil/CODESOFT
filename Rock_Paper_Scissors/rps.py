from random import choice


class RockPaperScissors:
    CHOICES = {'Rock': 'r', 'Paper': 'p', 'Scissors': 's'}

    def __init__(self, two_players=False, play_with_computer=False, rounds=3):
        self.rounds = rounds
        self.player1_score = 0
        self.player2_score = 0
        self.play_with_computer = play_with_computer
        self.two_players = two_players

        if not (two_players or play_with_computer):
            self.play_with_computer = True

        elif two_players and not play_with_computer:
            self.two_player = True

    def play(self):
        if self.play_with_computer:
            self.determine_winner("Player1 points", "Computer points", computer=True)
        elif self.two_player:
            self.determine_winner("Player1 points", "Player2 points", computer=False)

    def getchoice(self, msg):
        while True:
            p1 = input(f"{msg} enter your choice {list(self.CHOICES.keys())} 'r', 'p' or 's': ").lower()
            if p1 in self.CHOICES.values():
                return p1
            else:
                print("Enter from the given choices")
                continue

    def determine_winner(self, msg, msg2, computer=True):
        for _ in range(self.rounds):
            p1 = self.getchoice('Player 1').lower()
            if computer:
                p2 = choice(list(self.CHOICES.values()))
            else:
                p2 = self.getchoice('Player 2').lower()

            if p1 == p2:
                print(f"\n{msg}: {self.player1_score}")
                print(f"{msg2}: {self.player2_score}\n")
            elif (p1 == 'r' and p2 == 's') or (p1 == 's' and p2 == 'p') or (p1 == 'p' and p2 == 'r'):
                self.player1_score += 1
                print(f"\n{msg}: {self.player1_score}")
                print(f"{msg2}: {self.player2_score}\n")
            else:
                self.player2_score += 1
                print(f"\n{msg}: {self.player1_score}")
                print(f"{msg2}: {self.player2_score}\n")

        if self.player1_score > self.player2_score:
            print(f"{msg} wins the game with {self.player1_score} points")
        elif self.player1_score < self.player2_score:
            print(f"{msg2} wins the game with {self.player2_score} points")
        else:
            print("It's a tie!")

        self.player1_score = 0
        self.player2_score = 0
