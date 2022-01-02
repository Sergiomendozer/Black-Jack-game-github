"""
Table of contents
Variables
Variables for dealer count function
Function dealer_card_counter
Variables for User count function
Function user_card_counter
Function hit_or_stay
class color
Variables w/ emojis and card symbols
Lists function is to act as the deck but take out the cards the players are using
Strings below function are to show user dealer and user cards
List is a regular full deck of cards
For loop acts as a reshuffle, and in takes every element from full deck of card but makes it to be able to draw or delete a card
deals out first card to dealer
deals out first card to player
deals out second card to dealer
deals out second card to player
main prints
"""
# unless its a soft 17 soft is when there is an ace which is 11 or 1
# implement when ace is 11 or 1
# look at git hub code to find out how print (user_card_counter(dealer_total_count_hiddenstr,user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
# add a pause between certain actions

import random
#Variables
RED='\033[31m'
GREEN= '\033[1;32m'
Purple="\033[0;35m"
Cyan="\033[1;36m"
Yellow="\033[0;33m"
BLUE ="\033[0;34m"
PINK = "\033[1;31m"
END = '\033[0m'
flipped_over_card = "🃩"
S = "♠️"
C = "♣️"
D = RED + "♦️" + END
H = RED + "♥️" + END
K = "♚"
Q = '♛'
J= "Jack"
A = "Ace"
def shuffle_reshuffle(full_deck_of_cards,playing_deck):
        cards_left_in_deck = str(len(playing_deck))
        if len(playing_deck) < 13:
            while len(playing_deck) != 0:
                playing_deck.pop()
            (playing_deck)
            for e in full_deck_of_cards:
                playing_deck.append(e)
            print ("Cards have been shuffled since there were only "+ cards_left_in_deck + " left in the deck" )
            return (playing_deck)
        else:
            return (playing_deck)
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
    dealer_total_count_hiddenstr = str(dealer_card_counter_hidden(dealer_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
    print ("Dealers count: " + dealer_total_count_hiddenstr)
    print ("   Your Cards:" + users_cards)
    print (user_card_counter(dealer_total_count_hiddenstr,user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        

#Variables for dealer count function
dealer_cards_with_suits = [] 
dealer_cards_without_suits= [] 
dealer_total_count = 0
#Function separates suit from card number then counts the numbers for dealer
def dealer_card_counter(dealer_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards):
    dealer_cards_without_suits= []
    dealer_total_count = 0
    for e in dealer_cards_with_suits:
        if e.find("♛") !=-1:
            dealer_cards_without_suits.append(10)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):  
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_str= str(dealer_total_count)
                return (dealer_total_count_str)
        elif e.find("♚") !=-1:
            dealer_cards_without_suits.append(10)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):   
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_str= str(dealer_total_count)
                return (dealer_total_count_str)
        elif e.find("J") !=-1:
            dealer_cards_without_suits.append(10)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):  
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_str= str(dealer_total_count)
                return (dealer_total_count_str)
        elif e.find("A") !=-1:
            dealer_cards_without_suits.append(1)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits): 
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_str= str(dealer_total_count)
                return (dealer_total_count_str)
        elif e.find("♠️") != -1:
            spot= e.find("♠️")
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):  
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_str= str(dealer_total_count)
                return (dealer_total_count_str)
        elif e.find("♣️") != -1:
            spot= e.find("♣️")
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits): 
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_str= str(dealer_total_count)
                return (dealer_total_count_str)
        elif e.find(RED + "♦️" + END) != -1:
            spot = e.find(RED + "♦️" + END)
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):  
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_str= str(dealer_total_count)
                return (dealer_total_count_str)
        elif e.find(RED + "♥️" + END) !=-1:
            spot = e.find(RED + "♥️" + END)
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):  
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_str= str(dealer_total_count)
                return (dealer_total_count_str)

# dealer_cards_with_suits_hidden = [] 
dealer_cards_without_suits_hidden= [] 
dealer_total_count_hidden = 0
#Function separates suit from card number then counts the numbers for dealer
def dealer_card_counter_hidden(dealer_cards_with_suits_hidden,dealers_cards, dealers_cards_hidden,playing_deck,users_cards):
    dealer_cards_without_suits_hidden= []
    dealer_total_count_hidden = 0
    for e in dealer_cards_with_suits_hidden:
        if e.find("♛") !=-1:
            dealer_cards_without_suits_hidden.append(10)
            if len(dealer_cards_without_suits_hidden) == 1:  
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden= e
                    dealer_total_count_hiddenstr= str(dealer_total_count_hidden)
                return (dealer_total_count_hiddenstr)
        elif e.find("♚") !=-1:
            dealer_cards_without_suits_hidden.append(10)
            if len(dealer_cards_without_suits_hidden) == 1:     
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden= e
                    dealer_total_count_hiddenstr= str(dealer_total_count_hidden)
                return (dealer_total_count_hiddenstr)
        elif e.find("J") !=-1:
            dealer_cards_without_suits_hidden.append(10)
            if len(dealer_cards_without_suits_hidden) == 1:    
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden= e
                    dealer_total_count_hiddenstr= str(dealer_total_count_hidden)
                return (dealer_total_count_hiddenstr)
        elif e.find("A") !=-1:
            dealer_cards_without_suits_hidden.append(1)
            if len(dealer_cards_without_suits_hidden) == 1:   
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden= e
                    dealer_total_count_hiddenstr= str(dealer_total_count_hidden)
                return (dealer_total_count_hiddenstr)
        elif e.find("♠️") != -1:
            spot= e.find("♠️")
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:    
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden= e
                    dealer_total_count_hiddenstr= str(dealer_total_count_hidden)
                return (dealer_total_count_hiddenstr)
        elif e.find("♣️") != -1:
            spot= e.find("♣️")
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:   
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden= e
                    dealer_total_count_hiddenstr= str(dealer_total_count_hidden)
                return (dealer_total_count_hiddenstr)
        elif e.find(RED + "♦️" + END) != -1:
            spot = e.find(RED + "♦️" + END)
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:    
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden= e
                    dealer_total_count_hiddenstr= str(dealer_total_count_hidden)
                return (dealer_total_count_hiddenstr)
        elif e.find(RED + "♥️" + END) !=-1:
            spot = e.find(RED + "♥️" + END)
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:    
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden= e
                    dealer_total_count_hiddenstr= str(dealer_total_count_hidden)
                return (dealer_total_count_hiddenstr)
#Variables for User count function
#list keeps track of users cards to later separate the suits from number to be able to count 
user_cards_with_suits = []
user_cards_without_suits = [] 
user_total_count = 0
#function separates suit from card number then counts the numbers for user
def user_card_counter(dealer_total_count_hiddenstr,dealer_cards_with_suits_hidden,user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards):
    user_cards_without_suits = [] 
    user_total_count = 0
    for e in user_cards_with_suits:
        if e.find("♛") !=-1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (did_user_bust(dealer_total_count_hiddenstr,user_total_count,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        elif e.find("♚") !=-1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (did_user_bust(dealer_total_count_hiddenstr,user_total_count,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        elif e.find("J") !=-1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (did_user_bust(dealer_total_count_hiddenstr,user_total_count,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        elif e.find("A") !=-1:
            user_cards_without_suits.append(1)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (did_user_bust(dealer_total_count_hiddenstr,user_total_count,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        elif e.find("♠️") != -1:
            spot= e.find("♠️")
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (did_user_bust(dealer_total_count_hiddenstr,user_total_count,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        elif e.find("♣️") != -1:
            spot= e.find("♣️")
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (did_user_bust(dealer_total_count_hiddenstr,user_total_count,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        elif e.find(RED + "♦️" + END) != -1:
            spot = e.find(RED + "♦️" + END)
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (did_user_bust(dealer_total_count_hiddenstr,user_total_count,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        elif e.find(RED + "♥️" + END) !=-1:
            spot = e.find(RED + "♥️" + END)
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (did_user_bust(dealer_total_count_hiddenstr,user_total_count,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
def user_card_counter_2(dealers_cards, dealers_cards_hidden,playing_deck,users_cards):
    user_cards_without_suits = [] 
    user_total_count = 0
    for e in user_cards_with_suits:
        if e.find("♛") !=-1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (user_total_count)
        elif e.find("♚") !=-1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (user_total_count)
        elif e.find("J") !=-1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (user_total_count)
        elif e.find("A") !=-1:
            user_cards_without_suits.append(1)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (user_total_count)
        elif e.find("♠️") != -1:
            spot= e.find("♠️")
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (user_total_count)
        elif e.find("♣️") != -1:
            spot= e.find("♣️")
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (user_total_count)
        elif e.find(RED + "♦️" + END) != -1:
            spot = e.find(RED + "♦️" + END)
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (user_total_count)
        elif e.find(RED + "♥️" + END) !=-1:
            spot = e.find(RED + "♥️" + END)
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) ==  len(user_cards_without_suits):   
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count= user_total_count + e
                return (user_total_count)
#Function that see's if user went over 21
def did_user_bust(dealer_total_count_hiddenstr,user_total_count,dealers_cards, dealers_cards_hidden,playing_deck,users_cards):
    if user_total_count <= 21:
        user_total_count_str= str(user_total_count)
        print ("Your count is: " + user_total_count_str)
        x = str(input("Hit(H) or Stay(S):")) #### add add add to if below 21,add to bust function , user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards, x
        return hit_or_stay(dealer_total_count_hiddenstr,user_cards_with_suits, dealers_cards, dealers_cards_hidden,playing_deck,users_cards, x)
    elif user_total_count > 21:
        user_total_count= str(user_total_count)
        print ("   Your count: "+ user_total_count +RED+" which is over 21 so you bust, you lost"+ END)
        (play_again(playing_deck))

# function will act as dealer and in rules of Blackjack the dealer does not hit over 17 unless soft, soft is if there is an ace
def does_dealer_hit(user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards):
    dealer_total_count_str = (dealer_card_counter(dealer_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
    dealer_total_count_int= int(dealer_total_count_str) 
    print (Purple + "Dealer is now playing" + END)
    if dealer_total_count_int <= 17:
        print(Cyan+"Dealer hit"+END)
        chosen_card= random.choice(playing_deck)
        take_out_of_deck = playing_deck.index(chosen_card)
        playing_deck.pop(take_out_of_deck)
        chosen_card = str(chosen_card)
        dealer_cards_with_suits.append(chosen_card)
        dealers_cards= dealers_cards + chosen_card
        print ("Dealers Cards:" + dealers_cards) ###### delete later
        dealer_total_count_str = (dealer_card_counter(dealer_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        print ("Dealers count: " + dealer_total_count_str)
        print ("   Your Cards:" + users_cards)
        user_total_count_str=str(user_card_counter_2(dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        print ("Your count is: " + user_total_count_str)
        return (does_dealer_hit(user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
    else:
        print(Yellow + "Dealer Stays" + END)
        dealer_total_count = int(dealer_card_counter(dealer_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        #dealer_total_count = int(dealer_total_count_str)
        user_total_count =int(user_card_counter_2(dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        if dealer_total_count > 21:
            print ("Dealers count: " + dealer_total_count_str)
            print ("Dealer busted," + GREEN + "You win!" + END) #add here
            (play_again(playing_deck))
        elif dealer_total_count > user_total_count:
            print(BLUE+"Dealer wins"+END) #add here
            (play_again(playing_deck))
        elif user_total_count > dealer_total_count:
            print (GREEN + "You win!" + END) #add here
            (play_again(playing_deck))
        elif user_total_count == dealer_total_count:
            print("You pushed") #add here
            (play_again(playing_deck))

        

#function takes input of user to see if user wants to hit or stay
def hit_or_stay(dealer_total_count_hiddenstr,user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards, x):###maybe add a R for recomendation like what the book sas to do
    if x == "s" or x == "S" or x == "Stay" or x == "Stay" :
        return (does_dealer_hit(user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
    elif x == "H" or x == "h" or x == "Hit" or x == "hit":
        chosen_card= random.choice(playing_deck)
        take_out_of_deck = playing_deck.index(chosen_card)
        playing_deck.pop(take_out_of_deck)
        chosen_card = str(chosen_card)
        user_cards_with_suits.append(chosen_card)
        users_cards= users_cards + chosen_card
        print ("Dealers Cards:" + dealers_cards_hidden)
        # dealer_total_count_str = (dealer_card_counter(dealer_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        # print ("Dealers count: " + dealer_total_count_str)
        print ("Dealers count: " + dealer_total_count_hiddenstr)
        print ("   Your Cards:" + users_cards)
        #(user_card_counter(dealer_total_count_hiddenstr,user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
        return (user_card_counter(dealer_total_count_hiddenstr,dealer_total_count_hiddenstr,user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
    else: 
        y= input('\033[31m'+"You must enter H or S or Hit or Stay:"+'\033[0m')
        hit_or_stay(user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards,y)

#Variables w/ emojis and card symbols
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
    # def shuffle_reshuffle(full_deck_of_cards,playing_deck):
    #     if len(playing_deck) < 51:
    #         for e in full_deck_of_cards:
    #             playing_deck.append(e)
    ###flipped_over_card = "🎚️" 
    ###flipped_over_card = "🃟"
    flipped_over_card = "🃩"
    #lists function is to act as the deck but take out the cards the players are using
    playing_deck = []

    #Strings below function are to show user dealer and user cards
    dealers_cards_hidden = " "
    dealers_cards= " "
    users_cards = " "
    dealer_cards_with_suits_hidden = []
    #the list is a regular full deck of cards
    full_deck_of_cards = [A+S, "2"+S, "3"+S, "4"+S, "5"+S, "6"+S, "7"+S, "8"+S, "9"+S, "10"+S, K+" "+S, Q+" "+S, J+S,A+C, "2"+C, "3"+C, "4"+C, "5"+C, "6"+C, "7"+C, "8"+C, "9"+C, "10"+C, K+" "+C, Q+" "+C, J+C,A+D, "2"+D, "3"+D, "4"+D, "5"+D, "6"+D, "7"+D, "8"+D, "9"+D, "10"+D, K+" "+D, Q+" "+D, J+D,A+H, "2"+H, "3"+H, "4"+H, "5"+H, "6"+H, "7"+H, "8"+H, "9"+H, "10"+H, K+" "+H, Q+" "+H, J+H]
    chosen_card= random.choice(full_deck_of_cards)
    #shuffles if needs it
    shuffle_reshuffle(full_deck_of_cards,playing_deck)
    #to draw and take out card that is used, to avoid having the same cards being played
    take_out_of_deck = playing_deck.index(chosen_card)
    playing_deck.pop(take_out_of_deck)

    #deals out first card to dealer
    chosen_card = str(chosen_card)
    #adds card to list to be able to count card later
    dealer_cards_with_suits.append(chosen_card)
    dealer_cards_with_suits_hidden.append(chosen_card)
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
    dealer_total_count_str = (dealer_card_counter(dealer_cards_with_suits, dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
    # print ("Dealers count: " + dealer_total_count_str)
    dealer_total_count_hiddenstr = (dealer_card_counter_hidden(dealer_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))
    print ("Dealers count: " + dealer_total_count_hiddenstr)
    print ("   Your Cards:" + users_cards)
    (user_card_counter(dealer_total_count_hiddenstr,dealer_cards_with_suits_hidden,user_cards_with_suits,dealers_cards, dealers_cards_hidden,playing_deck,users_cards))

