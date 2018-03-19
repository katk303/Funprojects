n random module
    import random

   # Create card types
    card_values = ["Ace of ","King of ","Queen of ","Jack of ","10 of ","9 of ","8 of ","7 of ","6 of ","5 of ","4 of ","3 of ","2 of "]

   # Create suits
    hearts = [s + "hearts" for s in card_values]
    clubs = [s + "clubs" for s in card_values]
    spades = [s + "spades" for s in card_values]
    diamonds = [s + "diamonds" for s in card_values]

   # Combine to create full deck of cards in each suit (list)
    deck = hearts+clubs+spades+diamonds

   # Assign values to each card (Number cards = face values; face cards = ascending from 11)
    scores = [14,13,12,11,10,9,8,7,6,5,4,3,2,14,13,12,11,10,9,8,7,6,5,4,3,2,14,13,12,11,10,9,8,7,6,5,4,3,2,14,13,12,11,10,9,8,7,6,5,4,3,2]

   # Create dictionary pairing cards with values
    game_deck = dict(zip(deck,scores))
   # print(game_deck) to check accuracy, if desired

   # Name players; default to "Player 1" and "Player 2" if no input
    player1 = input("Player 1 name: ")
    if len(player1) == 0:
        player1 = "Player 1"
    player2 = input("Player 2 Name: ")
    if len(player2) == 0:
        player2 = "Player 2"

   # Deal first hand
    hand_1 = random.sample(deck,26)

   # Function to create second hand without duplicates
    def second_hand(deck):
      hand_2_maker = []
      for s in deck:
        if s not in hand_1:
          hand_2_maker.append(s)
        else:
          hand_2_maker = hand_2_maker
      return hand_2_maker

   # Call function to deal second hand
    hand_2 = second_hand(deck)

   # Play game!
    def play_war(hand_1,hand_2):
      score_1 = 0
      score_2 = 0
      Hand = 1
      while len(hand_1)> 0:
        #if randint raises error, k defaults to 0 (there's always a 0th element)
        try:
            k = random.randint(1, (len(hand_1)-1))
            #print(k)
        except:
            k = 0
         # compete (1 2 3 war)
        print("Hand",Hand)
        input("1,2,3...WAR! Press Enter.")
         #if hand 1 card has bigger value, player 1 wins the round
        if game_deck[hand_1[k]] > game_deck[hand_2[k]]:
          print(player1,": ",hand_1[k])
          print(player2,": ",hand_2[k])
          print(player1, "wins!")
             # add 1 to player 1 score
          score_1 += 1
          Hand += 1
             #print scores
          print("Score is", player1, score_1, ",", player2, score_2)
             #print new line
          print("")
             #remove cards from play
          hand_1.pop(k)
          hand_2.pop(k)
             #if hand 2 has higher value, p2 wins
        elif game_deck[hand_1[k]] < game_deck[hand_2[k]]:
          print(player1, ": ", hand_1[k])
          print(player2,": ", hand_2[k])
          print(player2, "wins!")
             # add 1 to player 2 score
          score_2 += 1
          Hand += 1
          print("Score is", player1, score_1, ",", player2, score_2)
          # print new line
          print("")
             #remove cards from play
          hand_1.pop(k)
          hand_2.pop(k)
        else:
             #no one wins if the cards have the same value
          print(player1, ": ", hand_1[k])
          print(player2,": ", hand_2[k])
          print("It's a tie!")
          print("Score is", player1, score_1, ",", player2, score_2)
          Hand += 1
             # print new line
          print("")
          hand_1.pop(k)
          hand_2.pop(k)
      #when the length of hand_1 = 0, the game is over -- no cards left
      else:
        print("Game over! Score is", player1, score_1, ",", player2, score_2)
        if score_1 > score_2:
            print("Congratulations,",player1)
        elif score_1 < score_2:
            print("Congratulations,",player2)
        else:
            print("So evenly matched!")

    play_war(hand_1,hand_2)

