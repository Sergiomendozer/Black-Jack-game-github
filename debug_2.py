import random
def play_again(playing_deck):
    print(PINK +" A New Game has Started" + END)
    #add a pause 
    user_cards_with_suits = []
    dealer_cards_with_suits = [] 
    dealer_cards_with_suits_hidden = []
    dealers_cards_hidden = " "
    dealers_cards= " "
    users_cards = " "
    #the list is a regular full deck of cards
    full_deck_of_cards = [A+S, "2"+S, "3"+S, "4"+S, "5"+S, "6"+S, "7"+S, "8"+S, "9"+S, "10"+S, K+" "+S, Q+" "+S, J+S,A+C, "2"+C, "3"+C, "4"+C, "5"+C, "6"+C, "7"+C, "8"+C, "9"+C, "10"+C, K+" "+C, Q+" "+C, J+C,A+D, "2"+D, "3"+D, "4"+D, "5"+D, "6"+D, "7"+D, "8"+D, "9"+D, "10"+D, K+" "+D, Q+" "+D, J+D,A+H, "2"+H, "3"+H, "4"+H, "5"+H, "6"+H, "7"+H, "8"+H, "9"+H, "10"+H, K+" "+H, Q+" "+H, J+H]
    #shuffles if needs it
    playing_deck = (shuffle_reshuffle(full_deck_of_cards,playing_deck))
    chosen_card = random.choice(playing_deck)
    #to draw and take out card that is used, to avoid having the same cards being played
    take_out_of_deck = playing_deck.index(chosen_card)
    playing_deck.pop(take_out_of_deck)
    
    #deals out first card to dealer
    chosen_card = str(chosen_card)
    #adds card to list to be able to count card later
    dealer_cards_with_suits.append(chosen_card)
    dealer_cards_with_suits_hidden.append(chosen_card)
    #name 'dealer_cards_with_suits_hidden' is not defined ######
    dealers_cards= dealers_cards + chosen_card
    dealers_cards_hidden = dealers_cards_hidden + chosen_card

    #deals out first card to player
    chosen_card= random.choice(playing_deck)
    take_out_of_deck = playing_deck.index(chosen_card)
    #to draw and take out card that is used, to avoid having the same cards being played
    playing_deck.pop(take_out_of_deck)
    chosen_card = str(chosen_card)
    #adds card to list to be able to count card later
    user_cards_with_suits.append(chosen_card)
    users_cards= users_cards + chosen_card

    #deals out second card to dealer
    chosen_card= random.choice(playing_deck)
    take_out_of_deck = playing_deck.index(chosen_card)
    #to draw and take out card that is used, to avoid having the same cards being played
    playing_deck.pop(take_out_of_deck)
    chosen_card = str(chosen_card)
    #adds card to list to be able to count card later
    dealer_cards_with_suits.append(chosen_card)
    dealers_cards= dealers_cards + chosen_card
    dealers_cards_hidden = dealers_cards_hidden + flipped_over_card

    #deals out second card to player
    chosen_card= random.choice(playing_deck)
    take_out_of_deck = playing_deck.index(chosen_card)
    #to draw and take out card that is used, to avoid having the same cards being played
    playing_deck.pop(take_out_of_deck)
    chosen_card = str(chosen_card)
    #adds card to list to be able to count card later
    user_cards_with_suits.append(chosen_card)
    users_cards= users_cards + chosen_card

    #main prints
    print ("Dealers Cards:" + dealers_cards_hidden)
    dealer_total_count_str = (dealer_card_counter(dealer_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
    #print ("Dealers count: " + dealer_total_count_str)
    # print (dealer_cards_with_suits_hidden)
    dealer_total_count_hiddenstr = (dealer_card_counter_hidden(dealer_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
    print ("Dealers count: " + dealer_total_count_hiddenstr)
    print ("   Your Cards:" + users_cards)
    return (user_card_counter(dealer_total_count_hiddenstr,dealer_cards_with_suits_hidden,user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))