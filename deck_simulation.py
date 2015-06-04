from random import shuffle

deck = [x for x in range(0,29)]
deck.append('kill command')
deck.append('kill command')

shuffle(deck)

hand = []
for i in range(0,4):
    hand.append(deck.pop())

print('Hand:\n', hand)

redeal_check = input('choose which cards to replace\n')
swaps = redeal_check.split(' ')
swaps = list(map(int, swaps))
num_swaps = len(swaps)
swap_values = []

for i in range(0,num_swaps):
    swap_values.append(hand[swaps[i]])

for card in swap_values:
    hand.remove(card)
    deck.append(card)

for i in range(0,num_swaps):
    hand.append(deck.pop())

print('New hand:\n', hand)

while len(deck) > 0:
    input('hit enter to deal')
    print(deck.pop())
