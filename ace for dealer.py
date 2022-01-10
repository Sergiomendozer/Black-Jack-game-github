# dealer_cards_without_suits = [1,2,3] 
str_to_find_ace_dealer = ""
dealer_cards_without_suits = [1,2,3,11] 
for e in dealer_cards_without_suits:
        e= str(e)
        str_to_find_ace_dealer = str_to_find_ace_dealer + e
(str_to_find_ace_dealer)
if str_to_find_ace_dealer.find("11") != -1:
    is_there_an_ace_dealer = "YES"
else:
    is_there_an_ace_dealer= "NO"
