import cards

def load_cards(r, deck, input_format):
    for a_card in deck:
        r.set(input_format.format(a_card),'')

def load_both(r):
    load_cards(r, cards.black_cards, "black:{}")
    load_cards(r, cards.white_cards, "white:{}")
