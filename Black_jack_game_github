#### add list for user and dealer so it can count cards### NEXT, make new file count4_blackjack
#### add comment to count and this code!!!!!!!!
## in count program: add elif statement when flipped over card in list to convert to 0
#if over 21 say bust and stop 
#reshuffle
#when to reshuffle
#dealer can only hit on 16 check rule
import random
RED='\033[31m'
END = '\033[0m'
flipped_over_card = "🃩"
### needs  to take for than x, like the lists
########################make computer hit function#############################

#list keeps track of users cards to later separate the suits from number to be able to count 
user_cards_with_suits = [] 
user_cards_without_suits= [] 
user_total_count = 0
#function separates suit from card number then counts the numbers for user
def card_counter():
    user_total_count = 0
    for e in user_cards_with_suits:
        if e.find("♛") !=-1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                    user_total_count_str= str(user_total_count)
                print ("Your count is:" + user_total_count_str)
        elif e.find("♚") !=-1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                    user_total_count_str= str(user_total_count)
                print ("Your count is:" + user_total_count_str)
        elif e.find("J") !=-1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                    user_total_count_str= str(user_total_count)
                print ("Your count is:" + user_total_count_str)
        elif e.find("A") !=-1:
            user_cards_without_suits.append(1)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                    user_total_count_str= str(user_total_count)
                print ("Your count is:" + user_total_count_str)
        elif e.find("♠️") != -1:
            spot= e.find("♠️")
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                    user_total_count_str= str(user_total_count)
                print ("Your count is:" + user_total_count_str)
        elif e.find("♣️") != -1:
            spot= e.find("♣️")
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                    user_total_count_str= str(user_total_count)
                print ("Your count is:" + user_total_count_str)
        elif e.find(RED + "♦️" + END) != -1:
            spot = e.find(RED + "♦️" + END)
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                    user_total_count_str= str(user_total_count)
                print ("Your count is:" + user_total_count_str)
        elif e.find(RED + "♥️" + END) !=-1:
            spot = e.find(RED + "♥️" + END)
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                    user_total_count_str= str(user_total_count)
                print ("Your count is:" + user_total_count_str)
#function takes input of user to see if user wants to hit or stay
def hit_or_stay(dealers_cards, dealers_cards_hidden,playing_deck,users_cards, x):# maybe add a R for recomendation like what the book sas to do
    if x == "s" or x == "S" or x == "Stay" or x == "Stay" :
        print("stay")
    elif x == "H" or x == "h" or x == "Hit" or x == "hit":
        chosen_card= random.choice(playing_deck)
        take_out_of_deck = playing_deck.index(chosen_card)
        playing_deck.pop(take_out_of_deck)
        chosen_card = str(chosen_card)
        users_cards= users_cards + chosen_card
        print ("Dealers Cards:" + dealers_cards) ###### delete later
        print ("Dealers Cards:" + dealers_cards_hidden)
        print ("   Your Cards:" + users_cards)
        print (len(playing_deck)) ##### delete later
        x = str(input("Hit(H) or Stay(S):"))
        hit_or_stay(dealers_cards, dealers_cards_hidden,playing_deck,users_cards, x)
    else: 
        y= input('\033[31m'+"You must enter H or S or Hit or Stay:"+'\033[0m')
        hit_or_stay(dealers_cards, dealers_cards_hidden,playing_deck,users_cards,y)
#classes of color and card emojis
class color:
    RED='\033[31m'
    END = '\033[0m'
    S = "♠️"
    C = "♣️"
    D = RED + "♦️" + END
    H = RED + "♥️" + END
    K = "♚"
    Q = '♛'
    J= "Jack"
    A = "Ace"
    #flipped_over_card = "🎚️" 
    #flipped_over_card = "🃟"
    flipped_over_card = "🃩"
    #lists function is to act as the deck but take out the cards the players are using
    playing_deck = []
    #strings below function are to show user dealer and user cards
    dealers_cards_hidden = " "
    dealers_cards= " "
    users_cards = " "
    #the list is a regular full deck of cards
    full_deck_of_cards = [A+S, "2"+S, "3"+S, "4"+S, "5"+S, "6"+S, "7"+S, "8"+S, "9"+S, "10"+S, K+" "+S, Q+" "+S, J+S,A+C, "2"+C, "3"+C, "4"+C, "5"+C, "6"+C, "7"+C, "8"+C, "9"+C, "10"+C, K+" "+C, Q+" "+C, J+C,A+D, "2"+D, "3"+D, "4"+D, "5"+D, "6"+D, "7"+D, "8"+D, "9"+D, "10"+D, K+" "+D, Q+" "+D, J+D,A+H, "2"+H, "3"+H, "4"+H, "5"+H, "6"+H, "7"+H, "8"+H, "9"+H, "10"+H, K+" "+H, Q+" "+H, J+H]
    chosen_card= random.choice(full_deck_of_cards)
    #### rewrite function for loops 
    for e in full_deck_of_cards:
        playing_deck.append(e)
    take_out_of_deck = playing_deck.index(chosen_card)
    #to draw and take out card that is used, to avoid having the same cards being played
    playing_deck.pop(take_out_of_deck)
    #deals out first card to dealer
    chosen_card = str(chosen_card)
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
    # call count function 
    #card_counter()

    ##### to delete later##########
    # print (playing_deck)
    # print (full_deck_of_cards)
    #print ("Your count is:" + user_total_count_str)
    print(user_cards_with_suits)
    print(user_cards_without_suits)
    ########################### above to delete later
    print ("Dealers Cards:" + dealers_cards) ###### delete later
    print ("Dealers Cards:" + dealers_cards_hidden)
    print ("   Your Cards:" + users_cards)
    (card_counter())
    # print ("Your card count:") ((card_counter())) maybe delete
    print (len(playing_deck)) ##### delete later
    x = str(input("Hit(H) or Stay(S):"))
    hit_or_stay(dealers_cards, dealers_cards_hidden,playing_deck,users_cards, x)
