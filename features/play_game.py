from chatbot import say,get_command
import random

def game_play(voice):
    say("Lets Play ROCK PAPER SCISSORS !!",voice)
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while (i < 5):
        choose = ("rock", "paper", "scissors")  # Tuple
        com_choose = random.choice(choose)
        query = get_command().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                say("ROCK",voice)
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                say("paper",voice)
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                say("Scissors",voice)
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper"):
            if (com_choose == "rock"):
                say("ROCK",voice)
                Me_score += 1
                print(f"Score:- ME :- {Me_score + 1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                say("paper",voice)
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                say("Scissors",voice)
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                say("ROCK",voice)
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                say("paper",voice)
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                say("Scissors",voice)
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")
    if (Me_score > Com_score):
        say("YOU WON",voice)
    else:
        say("YOU LOST",voice)


