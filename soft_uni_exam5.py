deck_of_cards = input().split()
faro_shuffle = int(input())

for _ in range(faro_shuffle):
    midpoint = len(deck_of_cards) // 2

    first_half = deck_of_cards[:midpoint]
    second_half = deck_of_cards[midpoint:]

    interleaved_deck = []

    for card1, card2 in zip(first_half, second_half):
        interleaved_deck.append(card1)
        interleaved_deck.append(card2)
    
    deck_of_cards = interleaved_deck

print(deck_of_cards)
