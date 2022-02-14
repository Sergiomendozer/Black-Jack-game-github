def did_user_bust(
    dealer_total_count_hiddenstr,
    user_total_count,
    dealers_cards,
    dealers_cards_hidden,
    playing_deck,
    users_cards,
    user_cards_with_suits,
    is_there_an_ace,
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
