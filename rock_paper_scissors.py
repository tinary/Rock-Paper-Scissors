import a6module;

rock = "rock"
paper = "paper"
scissors = "scissors"
rock_and_paper = "rock+paper"
rock_and_scissors = "rock+scissors"
paper_and_scissors = "paper+scissors"
rock_and_paper_and_scissors = "rock+paper+scissors"
none = "none"

game_prompt = "Rock-Paper-Scissors, play! [rock,paper,scissors,end]: "
computer_plays = "Computer plays"
computer_wins = "Computer wins"
user_wins = "User wins"
tie_game = "Tie"
total_games = "total games:"
total_user_wins = "user wins:"
total_computer_wins = "computer wins:"
total_ties = "ties:"


# count_rps_win: int int int-> string
# Purpose: consuems 3 integers r,p and s which represents the number of wins crrespond to ("rock","paper","scissors").
# Produces the string corresponding to the moves that won the most games
# Examples: count_rps_win(2,4,1) => 'paper'
#           count_rps_win(2,4,2) => 'rock_and_scissors'
#           count_rps_win(1,1,1) => 'rock+paper+scissors'

def count_rps_win(r,p,s):
    if r == 0 and p == 0 and s == 0:
        return none
    if r > p and r > s:
        return rock
    if p > r and p > s:
        return paper
    if s > p and s > r:
        return scissors
    if r > p and s > p and r == s:
        return rock_and_scissors
    if p > r and s > r and p == s:
        return paper_and_scissors
    if r > s and p > s and r == p:
        return rock_and_paper
    else:
        return rock_and_paper_and_scissors



# play_game: int int int int int int int string -> string
# Purpose: game_type must be one of "random","rock","paper" and "scissors".
# When the consumes stirng is "random", the input will be random base on the 3 variable strings
# ("rock","paper","scissors"). When the consumes string is any of the three strings, the computer input
# will be the same as the consume stirng. Then accumulate the result of numbers to who wins the most.
# When the game is played, the output will display computer's input and display who won the current game.
# When user input "end" the game, the output will display number of played games, number of the user wins,
# number of computer wins, number of games were tied.

def play_game(game_plaied,user_won,comp_won,tied,rock_win,paper_win,scissors_win,s):
    user_input = raw_input (game_prompt)
    if user_input == "end":
        print total_games,str(game_plaied)
        print total_user_wins,str(user_won)
        print total_computer_wins,str(comp_won)
        print total_ties,str(tied)
        return count_rps_win (rock_win,paper_win,scissors_win)

    computer_input = a6module.rps_get_move(s)
    if user_input == "rock" and computer_input == "paper":
        print computer_plays,computer_input
        print computer_wins
        return play_game(game_plaied + 1,user_won,comp_won + 1,tied,rock_win,paper_win + 1,scissors_win,s)
    if user_input == "rock" and computer_input == "scissors":
        print computer_plays,computer_input
        print user_wins
        return play_game(game_plaied + 1,user_won + 1,comp_won,tied,rock_win + 1,paper_win,scissors_win,s)
    if user_input == "rock" and computer_input == "rock":
        print computer_plays,computer_input
        print tie_game
        return play_game(game_plaied + 1,user_won,comp_won,tied + 1,rock_win,paper_win,scissors_win,s)
    if user_input == "paper" and computer_input == "rock":
        print computer_plays,computer_input
        print user_wins
        return play_game(game_plaied + 1,user_won + 1,comp_won,tied,rock_win,paper_win + 1,scissors_win,s)
    if user_input == "paper" and computer_input == "scissors":
        print computer_plays,computer_input
        print computer_wins
        return play_game(game_plaied + 1,user_won,comp_won + 1,tied,rock_win,paper_win,scissors_win + 1,s)
    if user_input == "paper" and computer_input == "paper":
        print computer_plays,computer_input
        print tie_game
        return play_game(game_plaied + 1,user_won,comp_won,tied + 1,rock_win,paper_win,scissors_win,s)
    if user_input == "scissors" and computer_input == "paper":
        print computer_plays,computer_input
        print user_wins
        return play_game(game_plaied + 1,user_won + 1,comp_won,tied,rock_win,paper_win,scissors_win + 1,s)
    if user_input == "scissors" and computer_input == "rock":
        print computer_plays,computer_input
        print computer_wins
        return play_game(game_plaied + 1,user_won,comp_won + 1,tied,rock_win + 1,paper_win,scissors_win,s)
    else:
        print computer_plays,computer_input
        print tie_game
        return play_game(game_plaied + 1,user_won,comp_won,tied + 1,rock_win,paper_win,scissors_win,s)

# rock_paper_scissors: string -> string

def rock_paper_scissors(game_type):
    return play_game(0,0,0,0,0,0,0,game_type)
