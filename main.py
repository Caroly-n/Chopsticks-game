# Rules:
# Each player starts with 2 hands, 1 finger each.
# Each player gets one turn. on their turn, they can:
# Attack the opponent's hand, adding the number they have on the attacking hand to the chosen opponent's attacked hand.
# Or, they can split the total num of fingers on both their own hands into different numbers, but they cannot simply swap. This move can revive a dead hand
# Once a hand has 5 fingers, the hand dies.
# When a player has 2 dead hands, the other wins and the game ends


import numpy as np

# 2 players, starting with 1 finger on each hand; 2 hands.
player_hand = np.array([1, 1])
bot_hand = np.array([1, 1])
player_turn = 1
bot_turn = 0


def action_attack(player, bot): #attacking function
    which_hand = int(input("Which hand would you like to use (1/2)? "))
    which_opponent_hand = int(input("Which hand would you like to attack (1/2)? "))
    opponent_index = which_opponent_hand - 1
    taken_number = player[which_hand - 1]
    if (bot[opponent_index] == 0 or taken_number == 0):
        print("Illegal move.")
        return action_attack(player, bot)
    bot[opponent_index] = bot[opponent_index] + taken_number
    for i in range(2):
        if(bot[i-1] >= 5):
            bot[i-1] = (0)
    return player, bot

def action_split(player, bot): #splitting hand function
    total = player[0] + player[1]
    first_hand = int(input(f"How many fingers would you like your first hand to have (1-{total})? "))
    if (0 < first_hand < total):
        player[0] = first_hand
        player[1] = (total-first_hand)
        return player, bot
    else:
        action_split(player)

def make_move(player_array, bot_array, whose_turn): #function for whenever you have a move
    if (whose_turn == 1):
        decision = input ("Please make a move (attack/split): ")
    if (whose_turn == 0):
        bot_rando
    if decision == "attack":
        player, move = action_attack(player_array, bot_array, whose_turn)
    elif decision == "split":
        player, move = action_split (player_array, bot_array, whose_turn)
    return player, move
        
def continue_or_not(player_input, bot_input): #determines if the game is over
    if ((player_input[0] == 0) and (player_input[1] == 0)):
        return "I"
    elif ((bot_input[0] == 0) and (bot_input[1] == 0)):
        return "You"
    else:
        return True

while True:
    print (f"You have {player_hand}. I have {bot_hand}")
    player_hand, bot_hand = make_move(player_hand, bot_hand, player_turn) # Player's turn
    winner = continue_or_not(player_hand, bot_hand)
    if (winner != True):
        break
    player_hand, bot_hand = make_move(player_hand, bot_hand, bot_turn) # Bot's turn
    winner = continue_or_not(player_hand, bot_hand)
    if (winner != True):
        break

print(f"{winner} won! Good game!")
