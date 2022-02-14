from numpy import var


def did_dealer_bust():
    pass


def does_dealer_hit():
    pass  ## funciton in program


# dealer_total_count_str = dealer_card_counter(
#         dealer_cards_with_suits,
#         dealers_cards,
#         dealers_cards_hidden,
#         playing_deck,
#         users_cards,
#     ) # TODO: original

dealer_total_count_str, does_dealer_have_an_ace = dealer_card_counter(
    dealer_cards_with_suits,
    dealers_cards,
    dealers_cards_hidden,
    playing_deck,
    users_cards,
    does_dealer_have_an_ace,
)

does_dealer_have_an_ace = ""
