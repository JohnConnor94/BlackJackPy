# python 3.7.4
from lib.Card import Card
from lib.Dealer import Dealer
from lib.Hand import Hand

if __name__ == "__main__":
    # initialize the game

    game_over: bool = False  # player wants to exit
    # counters

    n_games = 0
    games_won = 0
    games_lost = 0
    dealer = Dealer()
    dealer.shuffle()
    # print("Player hand")
    # print(player_hand)
    # print("Dealer hand")
    # print(str(dealer_hand))

    print("BlackJack game is starting")
    while not game_over:
        busted = False  # player_hands exceeds 21
        more_cards = True  # for asking another card

        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(dealer.pop_card())
        dealer_hand.add_card(dealer.pop_card())
        player_hand.add_card(dealer.pop_card())
        dealer_hand.add_card(dealer.pop_card())
        n_games += 1

        print(f"Status: won = {games_won} / lost = {games_lost}")
        if games_lost > 0:
            print(f"Ratio won/lost = {games_won / games_lost * 100}%")
        print(f"Games number {n_games}")

        # player turn
        if player_hand.is_black_jack:
            print("You have a BlackJack!")
        else:
            while player_hand.points < 21 and more_cards:
                print(f"You have cards:{player_hand} = {player_hand.points} points.")
                ans = input("Do you want a card? Everything = Yes / N = No -> ")
                if ans == "":
                    ans = "yes"
                if ans.lower() == "n" or ans.lower() == "no":
                    more_cards = False
                else:
                    card = dealer.pop_card()
                    player_hand.add_card(card)
                    print(f"New card is {card.value}")
            if player_hand.points > 21:
                print("You busted!")
                busted = True
        print(f"Your cards: {player_hand} = {player_hand.points} points\n")

        # dealer turn
        if dealer_hand.points == 21 and not busted:
            print(f"Dealer has a BlackJack!")
            print(f"Cards: {dealer_hand}")
        else:
            while dealer_hand.points < 17:
                print(f"Dealer has cards:{dealer_hand} = {dealer_hand.points} points\nHe takes a card")
                temp = dealer.pop_card()
                dealer_hand.add_card(temp)
                print(f"New card is {temp}")

            if dealer_hand.points > 21:
                print("Dealer busted!")
            print(f"Dealer has cards:{dealer_hand} = {dealer_hand.points} points")

            if dealer_hand.is_black_jack and player_hand.is_black_jack:
                print("2 BlackJack -> Dealer wins")
                games_lost += 1
            elif dealer_hand.points < player_hand.points < 22 or dealer_hand.points > 21:
                print(f"You win with {player_hand.points} vs dealer's {dealer_hand.points} points!")
                games_won += 1
            elif busted:
                print(f"Dealer wins with because you busted!")
                games_lost += 1
            else:
                print(f"Dealer wins with {dealer_hand.points} vs yours {player_hand.points} points!")
                games_lost += 1

        repeat = input("Do you want to continue? Everything = Yes / N = No -> ")
        if repeat == "":
            repeat = "yes"
        if repeat.lower() == "n" or repeat.lower() == "no":
            game_over = True
        else:
            print("Very well...\n")
        pass

    print("\nResume:")
    if games_won == 0:
        print("No won games. What a shame...")
    else:
        print(f"Won games = {games_won}")
    if games_lost == 0:
        print("No lost games. Very impressive!")
    else:
        print(f"Lost games = {games_lost}")
        print(f"Ratio Won/Lost = {games_won / games_lost * 100}%")
    print("I hope to see you again!")
