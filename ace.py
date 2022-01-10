user_cards_without_suits = [1,2,3] 
str_to_find_ace = ""
# user_cards_without_suits = [1,2,3,11] 
for e in user_cards_without_suits:
        e= str(e)
        str_to_find_ace = str_to_find_ace + e
(str_to_find_ace)
if str_to_find_ace.find("11") != -1:
    is_there_an_ace = "YES"
    print(is_there_an_ace)
else:
    is_there_an_ace = "NO"
    print (is_there_an_ace)
