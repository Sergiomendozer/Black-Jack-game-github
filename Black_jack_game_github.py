import time
import random

# Variables
RED = "\033[31m"
GREEN = "\033[1;32m"
Purple = "\033[0;35m"
Cyan = "\033[1;36m"
Yellow = "\033[0;33m"
BLUE = "\033[0;34m"
PINK = "\033[1;31m"
END = "\033[0m"
flipped_over_card = "🃩"
S = "♠️"
C = "♣️"
D = RED + "♦️" + END
H = RED + "♥️" + END
K = "♚"
Q = "♛"
J = "Jack"
A = "Ace"
# function "shuffles" deck if card count is bellow 13, all function does is add all cards back to deck
def shuffle_reshuffle(full_deck_of_cards, playing_deck):
    cards_left_in_deck = str(len(playing_deck))
    if len(playing_deck) < 13:
        while len(playing_deck) != 0:
            playing_deck.pop()
        (playing_deck)
        for e in full_deck_of_cards:
            playing_deck.append(e)
        print(
            "Cards have been shuffled since there were only "
            + cards_left_in_deck
            + " left in the deck"
        )
        return playing_deck
    else:
        return playing_deck


# functions loops game and is able to reset game
def play_again(playing_deck):
    time.sleep(1)
    print(PINK + " A New Game has Started" + END)
    time.sleep(2)
    # add a pause
    # empty list and string reset games varables
    user_cards_with_suits = []
    dealer_cards_with_suits = []
    dealer_cards_with_suits_hidden = []
    dealers_cards_hidden = " "
    dealers_cards = " "
    users_cards = " "
    does_dealer_have_an_ace = " "
    # the list is a regular full deck of cards
    full_deck_of_cards = [
        A + S,
        "2" + S,
        "3" + S,
        "4" + S,
        "5" + S,
        "6" + S,
        "7" + S,
        "8" + S,
        "9" + S,
        "10" + S,
        K + " " + S,
        Q + " " + S,
        J + S,
        A + C,
        "2" + C,
        "3" + C,
        "4" + C,
        "5" + C,
        "6" + C,
        "7" + C,
        "8" + C,
        "9" + C,
        "10" + C,
        K + " " + C,
        Q + " " + C,
        J + C,
        A + D,
        "2" + D,
        "3" + D,
        "4" + D,
        "5" + D,
        "6" + D,
        "7" + D,
        "8" + D,
        "9" + D,
        "10" + D,
        K + " " + D,
        Q + " " + D,
        J + D,
        A + H,
        "2" + H,
        "3" + H,
        "4" + H,
        "5" + H,
        "6" + H,
        "7" + H,
        "8" + H,
        "9" + H,
        "10" + H,
        K + " " + H,
        Q + " " + H,
        J + H,
    ]
    # shuffles if needs it
    playing_deck = shuffle_reshuffle(full_deck_of_cards, playing_deck)
    chosen_card = random.choice(playing_deck)
    # to draw and take out card that is used, to avoid having the same cards being played
    take_out_of_deck = playing_deck.index(chosen_card)
    playing_deck.pop(take_out_of_deck)

    # deals out first card to dealer
    chosen_card = str(chosen_card)
    # adds card to list to be able to count card later
    dealer_cards_with_suits.append(chosen_card)
    dealer_cards_with_suits_hidden.append(chosen_card)
    dealers_cards = dealers_cards + chosen_card
    dealers_cards_hidden = dealers_cards_hidden + chosen_card

    # deals out first card to player
    chosen_card = random.choice(playing_deck)
    take_out_of_deck = playing_deck.index(chosen_card)
    # to draw and take out card that is used, to avoid having the same cards being played
    playing_deck.pop(take_out_of_deck)
    chosen_card = str(chosen_card)
    # adds card to list to be able to count card later
    user_cards_with_suits.append(chosen_card)
    users_cards = users_cards + chosen_card

    # deals out second card to dealer
    chosen_card = random.choice(playing_deck)
    take_out_of_deck = playing_deck.index(chosen_card)
    # to draw and take out card that is used, to avoid having the same cards being played
    playing_deck.pop(take_out_of_deck)
    chosen_card = str(chosen_card)
    # adds card to list to be able to count card later
    dealer_cards_with_suits.append(chosen_card)
    dealers_cards = dealers_cards + chosen_card
    dealers_cards_hidden = dealers_cards_hidden + flipped_over_card

    # deals out second card to player
    chosen_card = random.choice(playing_deck)
    take_out_of_deck = playing_deck.index(chosen_card)
    # to draw and take out card that is used, to avoid having the same cards being played
    playing_deck.pop(take_out_of_deck)
    chosen_card = str(chosen_card)
    # adds card to list to be able to count card later
    user_cards_with_suits.append(chosen_card)
    users_cards = users_cards + chosen_card

    # main prints
    print("Dealers Cards:" + dealers_cards_hidden)
    dealer_total_count_str, does_dealer_have_an_ace = dealer_card_counter(
        dealer_cards_with_suits,
        dealers_cards,
        dealers_cards_hidden,
        playing_deck,
        users_cards,
        does_dealer_have_an_ace,
    )
    # print ("Dealers count: " + dealer_total_count_str)
    # print (dealer_cards_with_suits_hidden)
    dealer_total_count_hiddenstr = dealer_card_counter_hidden(
        dealer_cards_with_suits,
        dealers_cards,
        dealers_cards_hidden,
        playing_deck,
        users_cards,
    )
    print("Dealers count: " + dealer_total_count_hiddenstr)
    time.sleep(1)
    print("   Your Cards:" + users_cards)
    return user_card_counter(
        dealer_total_count_hiddenstr,
        dealer_cards_with_suits_hidden,
        user_cards_with_suits,
        dealers_cards,
        dealers_cards_hidden,
        playing_deck,
        users_cards,
        does_dealer_have_an_ace,
        dealer_cards_with_suits,
    )


# Variables for dealer count function
dealer_cards_with_suits = []
dealer_cards_without_suits = []
dealer_total_count = 0
# Function separates suit from card number then counts the numbers for dealer
def dealer_card_counter(
    dealer_cards_with_suits,
    dealers_cards,
    dealers_cards_hidden,
    playing_deck,
    users_cards,
    does_dealer_have_an_ace,
):
    dealer_cards_without_suits = []
    dealer_total_count = 0
    dealer_str_to_find_ace = ""
    for e in dealer_cards_with_suits:
        if e.find("♛") != -1:
            dealer_cards_without_suits.append(10)
            if len(dealer_cards_with_suits) == len(dealer_cards_without_suits):
                for e in dealer_cards_without_suits:
                    e = str(e)
                    dealer_str_to_find_ace = dealer_str_to_find_ace + e
                (dealer_str_to_find_ace)
                if dealer_str_to_find_ace.find("11") != -1:
                    does_dealer_have_an_ace = "YES"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
                else:
                    does_dealer_have_an_ace = "NO"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace

        elif e.find("♚") != -1:
            dealer_cards_without_suits.append(10)
            if len(dealer_cards_with_suits) == len(dealer_cards_without_suits):
                for e in dealer_cards_without_suits:
                    e = str(e)
                    dealer_str_to_find_ace = dealer_str_to_find_ace + e
                (dealer_str_to_find_ace)
                if dealer_str_to_find_ace.find("11") != -1:
                    does_dealer_have_an_ace = "YES"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
                else:
                    does_dealer_have_an_ace = "NO"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
        elif e.find("J") != -1:
            dealer_cards_without_suits.append(10)
            if len(dealer_cards_with_suits) == len(dealer_cards_without_suits):
                for e in dealer_cards_without_suits:
                    e = str(e)
                    dealer_str_to_find_ace = dealer_str_to_find_ace + e
                (dealer_str_to_find_ace)
                if dealer_str_to_find_ace.find("11") != -1:
                    does_dealer_have_an_ace = "YES"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
                else:
                    does_dealer_have_an_ace = "NO"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
        elif e.find("A") != -1:
            dealer_cards_without_suits.append(11)
            if len(dealer_cards_with_suits) == len(dealer_cards_without_suits):
                for e in dealer_cards_without_suits:
                    e = str(e)
                    dealer_str_to_find_ace = dealer_str_to_find_ace + e
                (dealer_str_to_find_ace)
                if dealer_str_to_find_ace.find("11") != -1:
                    does_dealer_have_an_ace = "YES"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
                else:
                    does_dealer_have_an_ace = "NO"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
        elif e.find("♠️") != -1:
            spot = e.find("♠️")
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) == len(dealer_cards_without_suits):
                for e in dealer_cards_without_suits:
                    e = str(e)
                    dealer_str_to_find_ace = dealer_str_to_find_ace + e
                (dealer_str_to_find_ace)
                if dealer_str_to_find_ace.find("11") != -1:
                    does_dealer_have_an_ace = "YES"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
                else:
                    does_dealer_have_an_ace = "NO"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
        elif e.find("♣️") != -1:
            spot = e.find("♣️")
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) == len(dealer_cards_without_suits):
                for e in dealer_cards_without_suits:
                    e = str(e)
                    dealer_str_to_find_ace = dealer_str_to_find_ace + e
                (dealer_str_to_find_ace)
                if dealer_str_to_find_ace.find("11") != -1:
                    does_dealer_have_an_ace = "YES"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
                else:
                    does_dealer_have_an_ace = "NO"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
        elif e.find(RED + "♦️" + END) != -1:
            spot = e.find(RED + "♦️" + END)
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) == len(dealer_cards_without_suits):
                for e in dealer_cards_without_suits:
                    e = str(e)
                    dealer_str_to_find_ace = dealer_str_to_find_ace + e
                (dealer_str_to_find_ace)
                if dealer_str_to_find_ace.find("11") != -1:
                    does_dealer_have_an_ace = "YES"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
                else:
                    does_dealer_have_an_ace = "NO"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
        elif e.find(RED + "♥️" + END) != -1:
            spot = e.find(RED + "♥️" + END)
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) == len(dealer_cards_without_suits):
                for e in dealer_cards_without_suits:
                    e = str(e)
                    dealer_str_to_find_ace = dealer_str_to_find_ace + e
                (dealer_str_to_find_ace)
                if dealer_str_to_find_ace.find("11") != -1:
                    does_dealer_have_an_ace = "YES"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace
                else:
                    does_dealer_have_an_ace = "NO"
                    for e in dealer_cards_without_suits:
                        e = int(e)
                        dealer_total_count = dealer_total_count + e
                    dealer_total_count_str = str(dealer_total_count)
                    return dealer_total_count_str, does_dealer_have_an_ace


dealer_cards_without_suits_hidden = []
dealer_total_count_hidden = 0
# Function separates suit from card number then counts the numbers for dealer
def dealer_card_counter_hidden(
    dealer_cards_with_suits_hidden,
    dealers_cards,
    dealers_cards_hidden,
    playing_deck,
    users_cards,
):
    dealer_cards_without_suits_hidden = []
    dealer_total_count_hidden = 0
    for e in dealer_cards_with_suits_hidden:
        if e.find("♛") != -1:
            dealer_cards_without_suits_hidden.append(10)
            if len(dealer_cards_without_suits_hidden) == 1:
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden = e
                    dealer_total_count_hiddenstr = str(dealer_total_count_hidden)
                return dealer_total_count_hiddenstr
        elif e.find("♚") != -1:
            dealer_cards_without_suits_hidden.append(10)
            if len(dealer_cards_without_suits_hidden) == 1:
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden = e
                    dealer_total_count_hiddenstr = str(dealer_total_count_hidden)
                return dealer_total_count_hiddenstr
        elif e.find("J") != -1:
            dealer_cards_without_suits_hidden.append(10)
            if len(dealer_cards_without_suits_hidden) == 1:
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden = e
                    dealer_total_count_hiddenstr = str(dealer_total_count_hidden)
                return dealer_total_count_hiddenstr
        elif e.find("A") != -1:
            dealer_cards_without_suits_hidden.append(1)
            if len(dealer_cards_without_suits_hidden) == 1:
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden = e
                    dealer_total_count_hiddenstr = str(dealer_total_count_hidden)
                return dealer_total_count_hiddenstr
        elif e.find("♠️") != -1:
            spot = e.find("♠️")
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden = e
                    dealer_total_count_hiddenstr = str(dealer_total_count_hidden)
                return dealer_total_count_hiddenstr
        elif e.find("♣️") != -1:
            spot = e.find("♣️")
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden = e
                    dealer_total_count_hiddenstr = str(dealer_total_count_hidden)
                return dealer_total_count_hiddenstr
        elif e.find(RED + "♦️" + END) != -1:
            spot = e.find(RED + "♦️" + END)
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden = e
                    dealer_total_count_hiddenstr = str(dealer_total_count_hidden)
                return dealer_total_count_hiddenstr
        elif e.find(RED + "♥️" + END) != -1:
            spot = e.find(RED + "♥️" + END)
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden = e
                    dealer_total_count_hiddenstr = str(dealer_total_count_hidden)
                return dealer_total_count_hiddenstr


# Variables for User count function
# list keeps track of users cards to later separate the suits from number to be able to count
user_cards_with_suits = []
user_cards_without_suits = []
user_total_count = 0
# function separates suit from card number then counts the numbers for user
def user_card_counter(
    dealer_total_count_hiddenstr,
    dealer_cards_with_suits_hidden,
    user_cards_with_suits,
    dealers_cards,
    dealers_cards_hidden,
    playing_deck,
    users_cards,
    does_dealer_have_an_ace,
    dealer_cards_with_suits,
):
    user_cards_without_suits = []
    user_total_count = 0
    str_to_find_ace = ""
    for e in user_cards_with_suits:
        if e.find("♛") != -1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = str(e)
                    str_to_find_ace = str_to_find_ace + e
                (str_to_find_ace)
                if str_to_find_ace.find("11") != -1:
                    is_there_an_ace = "YES"
                else:
                    is_there_an_ace = "NO"
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return did_user_bust(
                    dealer_total_count_hiddenstr,
                    user_total_count,
                    dealers_cards,
                    dealers_cards_hidden,
                    playing_deck,
                    users_cards,
                    user_cards_with_suits,
                    is_there_an_ace,
                    does_dealer_have_an_ace,
                    dealer_cards_with_suits,
                )
        elif e.find("♚") != -1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = str(e)
                    str_to_find_ace = str_to_find_ace + e
                (str_to_find_ace)
                if str_to_find_ace.find("11") != -1:
                    is_there_an_ace = "YES"
                else:
                    is_there_an_ace = "NO"
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return did_user_bust(
                    dealer_total_count_hiddenstr,
                    user_total_count,
                    dealers_cards,
                    dealers_cards_hidden,
                    playing_deck,
                    users_cards,
                    user_cards_with_suits,
                    is_there_an_ace,
                    does_dealer_have_an_ace,
                    dealer_cards_with_suits,
                )
        elif e.find("J") != -1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = str(e)
                    str_to_find_ace = str_to_find_ace + e
                (str_to_find_ace)
                if str_to_find_ace.find("11") != -1:
                    is_there_an_ace = "YES"
                else:
                    is_there_an_ace = "NO"
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return did_user_bust(
                    dealer_total_count_hiddenstr,
                    user_total_count,
                    dealers_cards,
                    dealers_cards_hidden,
                    playing_deck,
                    users_cards,
                    user_cards_with_suits,
                    is_there_an_ace,
                    does_dealer_have_an_ace,
                    dealer_cards_with_suits,
                )
        elif e.find("A") != -1:
            user_cards_without_suits.append(11)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = str(e)
                    str_to_find_ace = str_to_find_ace + e
                (str_to_find_ace)
                if str_to_find_ace.find("11") != -1:
                    is_there_an_ace = "YES"
                else:
                    is_there_an_ace = "NO"
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return did_user_bust(
                    dealer_total_count_hiddenstr,
                    user_total_count,
                    dealers_cards,
                    dealers_cards_hidden,
                    playing_deck,
                    users_cards,
                    user_cards_with_suits,
                    is_there_an_ace,
                    does_dealer_have_an_ace,
                    dealer_cards_with_suits,
                )
        elif e.find("♠️") != -1:
            spot = e.find("♠️")
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = str(e)
                    str_to_find_ace = str_to_find_ace + e
                (str_to_find_ace)
                if str_to_find_ace.find("11") != -1:
                    is_there_an_ace = "YES"
                else:
                    is_there_an_ace = "NO"
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return did_user_bust(
                    dealer_total_count_hiddenstr,
                    user_total_count,
                    dealers_cards,
                    dealers_cards_hidden,
                    playing_deck,
                    users_cards,
                    user_cards_with_suits,
                    is_there_an_ace,
                    does_dealer_have_an_ace,
                    dealer_cards_with_suits,
                )
        elif e.find("♣️") != -1:
            spot = e.find("♣️")
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = str(e)
                    str_to_find_ace = str_to_find_ace + e
                (str_to_find_ace)
                if str_to_find_ace.find("11") != -1:
                    is_there_an_ace = "YES"
                else:
                    is_there_an_ace = "NO"
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return did_user_bust(
                    dealer_total_count_hiddenstr,
                    user_total_count,
                    dealers_cards,
                    dealers_cards_hidden,
                    playing_deck,
                    users_cards,
                    user_cards_with_suits,
                    is_there_an_ace,
                    does_dealer_have_an_ace,
                    dealer_cards_with_suits,
                )
        elif e.find(RED + "♦️" + END) != -1:
            spot = e.find(RED + "♦️" + END)
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = str(e)
                    str_to_find_ace = str_to_find_ace + e
                (str_to_find_ace)
                if str_to_find_ace.find("11") != -1:
                    is_there_an_ace = "YES"
                else:
                    is_there_an_ace = "NO"
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return did_user_bust(
                    dealer_total_count_hiddenstr,
                    user_total_count,
                    dealers_cards,
                    dealers_cards_hidden,
                    playing_deck,
                    users_cards,
                    user_cards_with_suits,
                    is_there_an_ace,
                    does_dealer_have_an_ace,
                    dealer_cards_with_suits,
                )
        elif e.find(RED + "♥️" + END) != -1:
            spot = e.find(RED + "♥️" + END)
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = str(e)
                    str_to_find_ace = str_to_find_ace + e
                (str_to_find_ace)
                if str_to_find_ace.find("11") != -1:
                    is_there_an_ace = "YES"
                else:
                    is_there_an_ace = "NO"
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return did_user_bust(
                    dealer_total_count_hiddenstr,
                    user_total_count,
                    dealers_cards,
                    dealers_cards_hidden,
                    playing_deck,
                    users_cards,
                    user_cards_with_suits,
                    is_there_an_ace,
                    does_dealer_have_an_ace,
                    dealer_cards_with_suits,
                )


def user_card_counter_2(dealers_cards, dealers_cards_hidden, playing_deck, users_cards):
    user_cards_without_suits = []
    user_total_count = 0
    for e in user_cards_with_suits:
        if e.find("♛") != -1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return user_total_count
        elif e.find("♚") != -1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return user_total_count
        elif e.find("J") != -1:
            user_cards_without_suits.append(10)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return user_total_count
        elif e.find("A") != -1:
            user_cards_without_suits.append(1)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return user_total_count
        elif e.find("♠️") != -1:
            spot = e.find("♠️")
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return user_total_count
        elif e.find("♣️") != -1:
            spot = e.find("♣️")
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return user_total_count
        elif e.find(RED + "♦️" + END) != -1:
            spot = e.find(RED + "♦️" + END)
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return user_total_count
        elif e.find(RED + "♥️" + END) != -1:
            spot = e.find(RED + "♥️" + END)
            e = e[:spot]
            user_cards_without_suits.append(e)
            if len(user_cards_with_suits) == len(user_cards_without_suits):
                for e in user_cards_without_suits:
                    e = int(e)
                    user_total_count = user_total_count + e
                return user_total_count


# Function that see's if user went over 21
def did_user_bust(
    dealer_total_count_hiddenstr,
    user_total_count,
    dealers_cards,
    dealers_cards_hidden,
    playing_deck,
    users_cards,
    user_cards_with_suits,
    is_there_an_ace,
    does_dealer_have_an_ace,
    dealer_cards_with_suits,
):
    if is_there_an_ace == "NO":
        if user_total_count <= 21:
            user_total_count_str = str(user_total_count)
            print("Your count is: " + user_total_count_str)
            time.sleep(1)
            x = str(input("Hit(H) or Stay(S):"))
            return hit_or_stay(
                dealer_total_count_hiddenstr,
                user_cards_with_suits,
                dealers_cards,
                dealers_cards_hidden,
                playing_deck,
                users_cards,
                x,
                does_dealer_have_an_ace,
                dealer_cards_with_suits,
            )
        elif user_total_count > 21:
            user_total_count = str(user_total_count)
            print(
                "   Your count: "
                + user_total_count
                + RED
                + " which is over 21 so you bust, you lost"
                + END
            )
            (play_again(playing_deck))
    elif is_there_an_ace == "YES":
        if user_total_count <= 21:
            user_total_count_str = str(user_total_count)
            print("Your count is: " + user_total_count_str)
            time.sleep(1)
            x = str(input("Hit(H) or Stay(S):"))
            return hit_or_stay(
                dealer_total_count_hiddenstr,
                user_cards_with_suits,
                dealers_cards,
                dealers_cards_hidden,
                playing_deck,
                users_cards,
                x,
                does_dealer_have_an_ace,
                dealer_cards_with_suits,
            )
        elif user_total_count > 21:
            user_total_count = user_total_count - 10
            if user_total_count <= 21:
                user_total_count_str = str(user_total_count)
                print("Your count is: " + user_total_count_str)
                time.sleep(1)
                x = str(input("Hit(H) or Stay(S):"))
                return hit_or_stay(
                    dealer_total_count_hiddenstr,
                    user_cards_with_suits,
                    dealers_cards,
                    dealers_cards_hidden,
                    playing_deck,
                    users_cards,
                    x,
                    does_dealer_have_an_ace,
                    dealer_cards_with_suits,
                )
            else:
                user_total_count = str(user_total_count)
                print(
                    "   Your count: "
                    + user_total_count
                    + RED
                    + " which is over 21 so you bust, you lost"
                    + END
                )
                (play_again(playing_deck))


# function will act as dealer and in rules of Blackjack the dealer does not hit over 17 unless soft, soft is if there is an ace
def does_dealer_hit(
    dealer_cards_with_suits,
    dealers_cards,
    dealers_cards_hidden,
    playing_deck,
    users_cards,
    does_dealer_have_an_ace,
):
    dealer_total_count_str, does_dealer_have_an_ace = dealer_card_counter(
        dealer_cards_with_suits,
        dealers_cards,
        dealers_cards_hidden,
        playing_deck,
        users_cards,
        does_dealer_have_an_ace,
    )
    dealer_total_count_int = int(dealer_total_count_str)
    print(Purple + "Dealer is now playing" + END)
    time.sleep(4)
    if dealer_total_count_int <= 17:
        print(Cyan + "Dealer hit" + END)
        time.sleep(2)
        chosen_card = random.choice(playing_deck)
        take_out_of_deck = playing_deck.index(chosen_card)
        playing_deck.pop(take_out_of_deck)
        chosen_card = str(chosen_card)
        dealer_cards_with_suits.append(chosen_card)
        dealers_cards = dealers_cards + chosen_card
        print("Dealers Cards:" + dealers_cards)
        dealer_total_count_str = str(dealer_total_count_int)
        print("Dealers count: " + dealer_total_count_str)
        print("   Your Cards:" + users_cards)
        user_total_count_str = str(
            user_card_counter_2(
                dealers_cards, dealers_cards_hidden, playing_deck, users_cards
            )
        )
        print("Your count is: " + user_total_count_str)
        return does_dealer_hit(
            dealer_cards_with_suits,
            dealers_cards,
            dealers_cards_hidden,
            playing_deck,
            users_cards,
            does_dealer_have_an_ace,
        )
    elif dealer_total_count_int > 21 and does_dealer_have_an_ace == "NO":
        print(Yellow + "Dealer Stays" + END)
        time.sleep(1)
        print("Dealers Cards:" + dealers_cards)
        user_total_count = int(
            user_card_counter_2(
                dealers_cards, dealers_cards_hidden, playing_deck, users_cards
            )
        )
        print("Dealers count: " + dealer_total_count_str)
        time.sleep(1)
        print("Dealer busted," + GREEN + "You win!" + END)
        (play_again(playing_deck))
    elif dealer_total_count_int > 21 and does_dealer_have_an_ace == "Yes":
        dealer_total_count_int = int(dealer_total_count_str)
        dealer_total_count_int = dealer_total_count_int - 10
        dealer_total_count_str = str(dealer_total_count_int)
        user_total_count = int(
            user_card_counter_2(
                dealers_cards, dealers_cards_hidden, playing_deck, users_cards
            )
        )
        if dealer_total_count_int > user_total_count:
            print("Dealers count: " + dealer_total_count_str)
            time.sleep(1)
            print(BLUE + "Dealer wins" + END)
            (play_again(playing_deck))
        elif user_total_count > dealer_total_count_int:
            print("Dealers count: " + dealer_total_count_str)
            time.sleep(1)
            print(GREEN + "You win!" + END)
            (play_again(playing_deck))
        elif user_total_count == dealer_total_count_int:
            print("You pushed")
            (play_again(playing_deck))
        elif dealer_total_count_int > user_total_count:
            print("Dealers count: " + dealer_total_count_str)
            time.sleep(1)
            print(BLUE + "Dealer wins" + END)
            (play_again(playing_deck))
        elif user_total_count > dealer_total_count_int:
            print("Dealers count: " + dealer_total_count_str)
            time.sleep(1)
            print("Dealer busted," + GREEN + "You win!" + END)
            (play_again(playing_deck))
        elif user_total_count == dealer_total_count_int:
            print("Dealers count: " + dealer_total_count_str)
            print("You pushed")
            (play_again(playing_deck))
    else:
        print(Yellow + "Dealer Stays" + END)
        dealer_total_count, does_dealer_have_an_ace = dealer_card_counter(
            dealer_cards_with_suits,
            dealers_cards,
            dealers_cards_hidden,
            playing_deck,
            users_cards,
            does_dealer_have_an_ace,
        )
        dealer_total_count = int(dealer_total_count)
        user_total_count = int(
            user_card_counter_2(
                dealers_cards, dealers_cards_hidden, playing_deck, users_cards
            )
        )
        if dealer_total_count > user_total_count:
            print("Dealers count: " + dealer_total_count_str)
            time.sleep(1)
            print(BLUE + "Dealer wins" + END)
            (play_again(playing_deck))
        elif user_total_count > dealer_total_count:
            print("Dealers count: " + dealer_total_count_str)
            time.sleep(1)
            print(GREEN + "You win!" + END)
            (play_again(playing_deck))
        elif user_total_count == dealer_total_count:
            print("You pushed")
            (play_again(playing_deck))
        elif dealer_total_count > user_total_count:
            print("Dealers count: " + dealer_total_count_str)
            time.sleep(1)
            print(BLUE + "Dealer wins" + END)
            (play_again(playing_deck))
        elif user_total_count > dealer_total_count:
            print("Dealers count: " + dealer_total_count_str)
            time.sleep(1)
            print(GREEN + "You win!" + END)
            (play_again(playing_deck))
        elif user_total_count == dealer_total_count:
            print("You pushed")
            (play_again(playing_deck))


# function takes input of user to see if user wants to hit or stay
def hit_or_stay(
    dealer_total_count_hiddenstr,
    user_cards_with_suits,
    dealers_cards,
    dealers_cards_hidden,
    playing_deck,
    users_cards,
    x,
    does_dealer_have_an_ace,
    dealer_cards_with_suits,
):
    if x == "s" or x == "S" or x == "Stay" or x == "stay":
        return does_dealer_hit(
            dealer_cards_with_suits,
            dealers_cards,
            dealers_cards_hidden,
            playing_deck,
            users_cards,
            does_dealer_have_an_ace,
        )
    elif x == "H" or x == "h" or x == "Hit" or x == "hit":
        chosen_card = random.choice(playing_deck)
        take_out_of_deck = playing_deck.index(chosen_card)
        playing_deck.pop(take_out_of_deck)
        chosen_card = str(chosen_card)
        user_cards_with_suits.append(chosen_card)
        users_cards = users_cards + chosen_card
        print("Dealers Cards:" + dealers_cards_hidden)
        print("Dealers count: " + dealer_total_count_hiddenstr)
        print("   Your Cards:" + users_cards)
        return user_card_counter(
            dealer_total_count_hiddenstr,
            dealer_total_count_hiddenstr,
            user_cards_with_suits,
            dealers_cards,
            dealers_cards_hidden,
            playing_deck,
            users_cards,
            does_dealer_have_an_ace,
            dealer_cards_with_suits,
        )
    else:
        y = input("\033[31m" + "You must enter H or S or Hit or Stay:" + "\033[0m")
        return hit_or_stay(
            dealer_total_count_hiddenstr,
            user_cards_with_suits,
            dealers_cards,
            dealers_cards_hidden,
            playing_deck,
            users_cards,
            y,
            does_dealer_have_an_ace,
            dealer_cards_with_suits,
        )


# Variables w/ emojis and card symbols
class color:
    RED = "\033[31m"
    END = "\033[0m"
    S = "♠️"
    C = "♣️"
    D = RED + "♦️" + END
    H = RED + "♥️" + END
    K = "♚"
    Q = "♛"
    J = "Jack"
    A = "Ace"
    # other back of card options: flipped_over_card = "🎚️" and flipped_over_card = "🃟"
    flipped_over_card = "🃩"
    # lists function is to act as the deck but take out the cards the players are using
    playing_deck = []
    # Strings below function are to show user dealer and user cards
    dealers_cards_hidden = " "
    dealers_cards = " "
    users_cards = " "
    does_dealer_have_an_ace = ""
    dealer_cards_with_suits_hidden = []
    # the list is a regular full deck of cards
    full_deck_of_cards = [
        A + S,
        "2" + S,
        "3" + S,
        "4" + S,
        "5" + S,
        "6" + S,
        "7" + S,
        "8" + S,
        "9" + S,
        "10" + S,
        K + " " + S,
        Q + " " + S,
        J + S,
        A + C,
        "2" + C,
        "3" + C,
        "4" + C,
        "5" + C,
        "6" + C,
        "7" + C,
        "8" + C,
        "9" + C,
        "10" + C,
        K + " " + C,
        Q + " " + C,
        J + C,
        A + D,
        "2" + D,
        "3" + D,
        "4" + D,
        "5" + D,
        "6" + D,
        "7" + D,
        "8" + D,
        "9" + D,
        "10" + D,
        K + " " + D,
        Q + " " + D,
        J + D,
        A + H,
        "2" + H,
        "3" + H,
        "4" + H,
        "5" + H,
        "6" + H,
        "7" + H,
        "8" + H,
        "9" + H,
        "10" + H,
        K + " " + H,
        Q + " " + H,
        J + H,
    ]
    chosen_card = random.choice(full_deck_of_cards)
    # shuffles if needs it
    shuffle_reshuffle(full_deck_of_cards, playing_deck)
    # to draw and take out card that is used, to avoid having the same cards being played
    take_out_of_deck = playing_deck.index(chosen_card)
    playing_deck.pop(take_out_of_deck)

    # deals out first card to dealer
    chosen_card = str(chosen_card)
    # adds card to list to be able to count card later
    dealer_cards_with_suits.append(chosen_card)
    dealer_cards_with_suits_hidden.append(chosen_card)
    dealers_cards = dealers_cards + chosen_card
    dealers_cards_hidden = dealers_cards_hidden + chosen_card

    # deals out first card to player
    chosen_card = random.choice(playing_deck)
    take_out_of_deck = playing_deck.index(chosen_card)
    # to draw and take out card that is used, to avoid having the same cards being played
    playing_deck.pop(take_out_of_deck)
    chosen_card = str(chosen_card)
    # adds card to list to be able to count card later
    user_cards_with_suits.append(chosen_card)
    users_cards = users_cards + chosen_card

    # deals out second card to dealer
    chosen_card = random.choice(playing_deck)
    take_out_of_deck = playing_deck.index(chosen_card)
    # to draw and take out card that is used, to avoid having the same cards being played
    playing_deck.pop(take_out_of_deck)
    chosen_card = str(chosen_card)
    # adds card to list to be able to count card later
    dealer_cards_with_suits.append(chosen_card)
    dealers_cards = dealers_cards + chosen_card
    dealers_cards_hidden = dealers_cards_hidden + flipped_over_card

    # deals out second card to player
    chosen_card = random.choice(playing_deck)
    take_out_of_deck = playing_deck.index(chosen_card)
    # to draw and take out card that is used, to avoid having the same cards being played
    playing_deck.pop(take_out_of_deck)
    chosen_card = str(chosen_card)
    # adds card to list to be able to count card later
    user_cards_with_suits.append(chosen_card)
    users_cards = users_cards + chosen_card

    # main prints
    print("Dealers Cards:" + dealers_cards_hidden)
    dealer_total_count_str, does_dealer_have_an_ace = dealer_card_counter(
        dealer_cards_with_suits,
        dealers_cards,
        dealers_cards_hidden,
        playing_deck,
        users_cards,
        does_dealer_have_an_ace,
    )
    # print ("Dealers count: " + dealer_total_count_str)
    dealer_total_count_hiddenstr = dealer_card_counter_hidden(
        dealer_cards_with_suits,
        dealers_cards,
        dealers_cards_hidden,
        playing_deck,
        users_cards,
    )
    print("Dealers count: " + dealer_total_count_hiddenstr)
    time.sleep(1)
    print("   Your Cards:" + users_cards)
    (
        user_card_counter(
            dealer_total_count_hiddenstr,
            dealer_cards_with_suits_hidden,
            user_cards_with_suits,
            dealers_cards,
            dealers_cards_hidden,
            playing_deck,
            users_cards,
            does_dealer_have_an_ace,
            dealer_cards_with_suits,
        )
    )
