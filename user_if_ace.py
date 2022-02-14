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
                )