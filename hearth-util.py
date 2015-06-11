import sys

def get_class_cards(class_type):
    start = chomped.index(class_type)
    indices = [
        i for i, 
        x in enumerate(chomped) if x == '----------' and i > start+1]
    end = indices[0]
    subset = chomped[start+2:end]
    results = [x for x in subset if x]
    rarity = [x.split(' ')[-1].strip('()') for x in results]
    cost = get_cost(rarity)
    print(class_type + ' (' + str(len(results)) + ' cards, ' + \
          str(cost) + ' dust):')
    for item in results:
        print(item)
    print()

def get_rarity_cards(rarity):
    results = [x.rsplit(' ', 1)[0] for x in chomped if rarity in x]
    types = [rarity] * len(results)
    cost = get_cost(types)
    print(rarity + ' (' + str(len(results)) + ' cards, ' + \
          str(cost) + ' dust):')
    for line in results:
        print(line)
    print()

def get_cost(rarity):
    total = 0
    for item in rarity:
        if item == 'Legendary':
            total += 1600
        elif item == 'Epic':
            total += 400
        elif item == 'Rare':
            total += 100
        elif item == 'Common':
            total += 40
    return total

if __name__ == "__main__":

    lines = []
    filename = 'missing.txt'
    rarities = ['legendary', 'l', 'epic', 'e', 'rare', 'r', 'common', 'c']
    classes = ['druid', 'd', 'hunter', 'h', 'mage', 'm',
               'paladin', 'pa', 'priest', 'pr', 'rogue', 'ro',
               'shaman', 's', 'warlock', 'wl', 'warrior', 'wr']

    if len(sys.argv) < 1 or len(sys.argv) > 2:
        print("Usage: python3 hearth-util [--help or -h]")
        sys.exit(1)
    elif len(sys.argv) == 2:
        if sys.argv[1] != "-h" and sys.argv[1] != "--help":
            print("Usage: python3 hearth-util [--help or -h]")
            sys.exit(1)
        else:
            print("Hearthstone Utiltity (hearth-util) Help:")
            print()

            print("Possible rarities:")
            count = 1
            first = True
            for i, item in enumerate(rarities):
                if count >= 5:
                    print("")
                    count = 1
                if i == len(rarities) - 1:
                    print(item, end="")
                else:
                    print(item + ",", "", end="")
                    count += 1

            print("\n")

            print("Possible classes:")
            count = 1
            for i, item in enumerate(classes):
                if count >= 5:
                    print()
                    count = 1
                if i == len(classes) - 1:
                    print(item, end="")
                else:
                    print(item + ",", "", end="")
                    count += 1

            print("\n")
            sys.exit(0)

    with open(filename) as f:
        lines = f.readlines()

    chomped = list(map(str.strip, lines))

    input_question = 'What kind of cards are you looking for?' + \
                     ' [type "exit" to quit]\n'

    user_input = ''
    while True:
        user_input = input(input_question).lower()
        if user_input == "exit":
            break
        print()
        if not any(word in user_input for word in rarities) and \
           not any(word in user_input for word in classes):
                print('Invalid filter type.',
                      'Use the --help command to view all valid filter types.')
        else:
            if user_input == 'd' or user_input == 'druid':
                get_class_cards('Druid')
            elif user_input == 'h' or user_input == 'hunter':
                get_class_cards('Hunter')
            elif user_input == 'm' or user_input == 'mage':
                get_class_cards('Mage')
            elif user_input == 'pa' or user_input == 'paladin':
                get_class_cards('Paladin')
            elif user_input == 'pr' or user_input == 'priest':
                get_class_cards('Priest')
            elif user_input == 'ro' or user_input == 'rogue':
                get_class_cards('Rogue')
            elif user_input == 's' or user_input == 'shaman':
                get_class_cards('Shaman')
            elif user_input == 'wl' or user_input == 'warlock':
                get_class_cards('Warlock')
            elif user_input == 'wr' or user_input == 'warrior':
                get_class_cards('Warrior')
            
            elif user_input == 'l' or user_input == 'legendary':
                get_rarity_cards('Legendary')
            elif user_input == 'e' or user_input == 'epic':
                get_rarity_cards('Epic')
            elif user_input == 'r' or user_input == 'rare':
                get_rarity_cards('Rare')
            elif user_input == 'c' or user_input == 'common':
                get_rarity_cards('Common')

