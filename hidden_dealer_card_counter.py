dealer_cards_with_suits_hidden = [] 
dealer_cards_without_suits_hidden= [] 
dealer_total_count_hidden = 0
#Function separates suit from card number then counts the numbers for dealer
def dealer_card_counter_hidden(dealer_cards_with_suits_hidden,dealers_cards, dealers_cards_hidden,playing_deck,users_cards):
    dealer_cards_without_suits_hidden_hidden= []
    dealer_total_count_hidden = 0
    for e in dealer_cards_with_suits_hidden:
        if e.find("♛") !=-1:
            dealer_cards_without_suits_hidden.append(10)
            if len(dealer_cards_without_suits_hidden) == 1:  
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count_hidden= dealer_total_count_hidden + e
                dealer_total_count_hiddenstr= str(dealer_total_count_hidden)
                return (dealer_total_count_hiddenstr)
        elif e.find("♚") !=-1:
            dealer_cards_without_suits_hidden.append(10)
            if len(dealer_cards_without_suits_hidden) == 1:     
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_hiddenstr= str(dealer_total_count)
                return (dealer_total_count_hiddenstr)
        elif e.find("J") !=-1:
            dealer_cards_without_suits_hidden.append(10)
            if len(dealer_cards_without_suits_hidden) == 1:    
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_hiddenstr= str(dealer_total_count)
                return (dealer_total_count_hiddenstr)
        elif e.find("A") !=-1:
            dealer_cards_without_suits_hidden.append(1)
            if len(dealer_cards_without_suits_hidden) == 1:   
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_hiddenstr= str(dealer_total_count)
                return (dealer_total_count_hiddenstr)
        elif e.find("♠️") != -1:
            spot= e.find("♠️")
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:    
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_hiddenstr= str(dealer_total_count)
                return (dealer_total_count_hiddenstr)
        elif e.find("♣️") != -1:
            spot= e.find("♣️")
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:   
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_hiddenstr= str(dealer_total_count)
                return (dealer_total_count_hiddenstr)
        elif e.find(RED + "♦️" + END) != -1:
            spot = e.find(RED + "♦️" + END)
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:    
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_hiddenstr= str(dealer_total_count)
                return (dealer_total_count_hiddenstr)
        elif e.find(RED + "♥️" + END) !=-1:
            spot = e.find(RED + "♥️" + END)
            e = e[:spot]
            dealer_cards_without_suits_hidden.append(e)
            if len(dealer_cards_without_suits_hidden) == 1:    
                for e in dealer_cards_without_suits_hidden:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                dealer_total_count_hiddenstr= str(dealer_total_count)
                return (dealer_total_count_hiddenstr)