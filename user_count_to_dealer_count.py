#list keeps track of dealers cards to later separate the suits from number to be able to count
dealer_cards_with_suits = [] 
dealer_cards_without_suits= [] 
dealer_total_count = 0
#function separates suit from card number then counts the numbers for dealer
def dealer_card_counter():
    dealer_total_count = 0
    for e in dealer_cards_with_suits:
        if e.find("♛") !=-1:
            dealer_cards_without_suits.append(10)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):   
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                    dealer_total_count_str= str(dealer_total_count)
                print ("Your count is:" + dealer_total_count_str)
        elif e.find("♚") !=-1:
            dealer_cards_without_suits.append(10)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):   
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                    dealer_total_count_str= str(dealer_total_count)
                print ("Your count is:" + dealer_total_count_str)
        elif e.find("J") !=-1:
            dealer_cards_without_suits.append(10)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):   
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                    dealer_total_count_str= str(dealer_total_count)
                print ("Your count is:" + dealer_total_count_str)
        elif e.find("A") !=-1:
            dealer_cards_without_suits.append(1)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):   
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                    dealer_total_count_str= str(dealer_total_count)
                print ("Your count is:" + dealer_total_count_str)
        elif e.find("♠️") != -1:
            spot= e.find("♠️")
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):   
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                    dealer_total_count_str= str(dealer_total_count)
                print ("Your count is:" + dealer_total_count_str)
        elif e.find("♣️") != -1:
            spot= e.find("♣️")
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):   
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                    dealer_total_count_str= str(dealer_total_count)
                print ("Your count is:" + dealer_total_count_str)
        elif e.find(RED + "♦️" + END) != -1:
            spot = e.find(RED + "♦️" + END)
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):   
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                    dealer_total_count_str= str(dealer_total_count)
                print ("Your count is:" + dealer_total_count_str)
        elif e.find(RED + "♥️" + END) !=-1:
            spot = e.find(RED + "♥️" + END)
            e = e[:spot]
            dealer_cards_without_suits.append(e)
            if len(dealer_cards_with_suits) ==  len(dealer_cards_without_suits):   
                for e in dealer_cards_without_suits:
                    e = int(e)
                    dealer_total_count= dealer_total_count + e
                    dealer_total_count_str= str(dealer_total_count)
                print ("Your count is:" + dealer_total_count_str)
