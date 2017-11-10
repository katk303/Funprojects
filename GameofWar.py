def main():

   # Play war
    import random
   # Create deck
    card_values = ["Ace of ","King of ","Queen of ","Jack of ","10 of ","9 of ","8 of ","7 of ","6 of ","5 of ","4 of ","3 of ","2 of "]
   # create suits
    hearts = [s + "hearts" for s in card_values]
    clubs = [s + "clubs" for s in card_values]
    spades = [s + "spades" for s in card_values]
    diamonds = [s + "diamonds" for s in card_values]
   # full deck
    deck = hearts+clubs+spades+diamonds
   # scores for each card
    scores = [13,12,11,10,9,8,7,6,5,4,3,2,1,13,12,11,10,9,8,7,6,5,4,3,2,1,13,12,11,10,9,8,7,6,5,4,3,2,1,13,12,11,10,9,8,7,6,5,4,3,2,1]
   # dictionary pairing scores with cards
    game_deck = dict(zip(deck,scores))
    # print(game_deck) 'to check
    # name players
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 Name: ")
   # get first hand
    hand_1 = random.sample(deck,26)
    #get non-duplicate hand_2
    def second_hand(deck):
      hand_2_maker = []
      for s in deck:
        if s not in hand_1:
          hand_2_maker.append(s)
        else:
          hand_2_maker = hand_2_maker
      return hand_2_maker


    hand_2 = second_hand(deck)

    def play_war(hand_1,hand_2):
      score_1 = 0
      score_2 = 0
      while len(hand_1)> 2:
         #get random index to randomize card chosen
        from random import randint
        k = randint(1, (len(hand_1)-1))
         # compete (1 2 3 war)
        print("1,2,3...WAR!")
         #if hand 1 card has bigger value, player 1 wins the round
        if game_deck[hand_1[k]] > game_deck[hand_2[k]]:
          print(player1,": ",hand_1[k])
          print(player2,": ",hand_2[k])
          print(player1, " wins!")
             # add 1 to player 1 score
          score_1 += 1
             #print scores
          print("Score is ", player1, " ", score_1, ", ", player2, " ", score_2)
             #remove cards from play
          hand_1.pop(k)
          hand_2.pop(k)
             #if hand 2 has higher value, p2 wins
        elif game_deck[hand_1[k]] < game_deck[hand_2[k]]:
          print(player1, ": ", hand_1[k])
          print(player2,": ", hand_2[k])
          print(player2, " wins!")
             # add 1 to player 2 score
          score_2 += 1
          print("Score is ", player1, " ", score_1, ", ", player2, " ", score_2)
             #remove cards from play
          hand_1.pop(k)
          hand_2.pop(k)
        else:
             #no one wins if the cards have the same value
          print(player1, ": ", hand_1[k])
          print(player2,": ", hand_2[k])
          print("It's a tie!")
          print("Score is ", player1, " ", score_1, ", ", player2, " ", score_2)
          hand_1.pop(k)
          hand_2.pop(k)
      #when the length of hand_1 = 0, the game is over -- no cards left
      else:
        print("Game over! Score is ", player1, " ", score_1, ", ", player2, " ", score_2)

    play_war(hand_1,hand_2)










if __name__ == "__main__":
    main()
