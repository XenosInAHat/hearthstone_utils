import sys

def get_class_cards(class_type, verbose, chomped):
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
    if verbose:
        for item in results:
            print(item)
    else:
        if len(results) != 0:
            print("[List of cards not shown]")
    print()

def get_rarity_cards(rarity, verbose, chomped):
    results = [x.rsplit(' ', 1)[0] for x in chomped if rarity in x]
    types = [rarity] * len(results)
    cost = get_cost(types)
    print(rarity + ' (' + str(len(results)) + ' cards, ' + \
          str(cost) + ' dust):')
    if verbose:
        for line in results:
            print(line)
    else:
        if len(results) != 0:
            print("[List of cards not shown]")
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

def output_help(rarities, classes):
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

def get_cards(user_input, verbose, chomped):
    if user_input == 'd' or user_input == 'druid':
        get_class_cards('Druid', verbose, chomped)
    elif user_input == 'h' or user_input == 'hunter':
        get_class_cards('Hunter', verbose, chomped)
    elif user_input == 'm' or user_input == 'mage':
        get_class_cards('Mage', verbose, chomped)
    elif user_input == 'pa' or user_input == 'paladin':
        get_class_cards('Paladin', verbose, chomped)
    elif user_input == 'pr' or user_input == 'priest':
        get_class_cards('Priest', verbose, chomped)
    elif user_input == 'ro' or user_input == 'rogue':
        get_class_cards('Rogue', verbose, chomped)
    elif user_input == 's' or user_input == 'shaman':
        get_class_cards('Shaman', verbose, chomped)
    elif user_input == 'wl' or user_input == 'warlock':
        get_class_cards('Warlock', verbose, chomped)
    elif user_input == 'wr' or user_input == 'warrior':
        get_class_cards('Warrior', verbose, chomped)
    
    elif user_input == 'l' or user_input == 'legendary':
        get_rarity_cards('Legendary', verbose, chomped)
    elif user_input == 'e' or user_input == 'epic':
        get_rarity_cards('Epic', verbose, chomped)
    elif user_input == 'r' or user_input == 'rare':
        get_rarity_cards('Rare', verbose, chomped)
    elif user_input == 'c' or user_input == 'common':
        get_rarity_cards('Common', verbose, chomped)

def check_cmd_input():
    if len(sys.argv) < 1 or len(sys.argv) > 2:
        print("Usage: python3 hearth-util [--help or -h]")
        sys.exit(1)
    elif len(sys.argv) == 2:
        if sys.argv[1] != "-h" and sys.argv[1] != "--help":
            print("Usage: python3 hearth-util [--help or -h]")
            sys.exit(1)
        else:
            output_help(rarities, classes)

def get_file_contents(filename):
    with open(filename) as f:
        lines = f.readlines()

    chomped = list(map(str.strip, lines))
    return chomped

def process_input(rarities, classes, chomped):
    input_question = 'What kind of cards are you looking for?' + \
                     ' [type "exit" to quit]\n'

    user_input = ''
    while True:
        user_input = input(input_question).lower()
        user_input_list = user_input.split()
        verbose = False
        if len(user_input_list) != 1:
            if user_input_list[1] != '-v' and user_input_list[1] != '--verbose':
                print("Invalid input. Check help for more info.")
                continue
            elif not any(word in user_input_list[0] for word in rarities) and \
                 not any(word in user_input_list[0] for word in classes):
                   print('Invalid filter type.',
                           'Use the --help command to view all valid filter types.')
            else:
                verbose = True
                user_input = user_input_list[0]

        if user_input == "exit":
            break
        print()
        if not any(word in user_input for word in rarities) and \
           not any(word in user_input for word in classes):
               print('Invalid filter type.',
                       'Use the --help command to view all valid filter types.')
        else:
            get_cards(user_input, verbose, chomped)

def main():
    lines = []
    filename = 'missing.txt'
    rarities = ['legendary', 'l', 'epic', 'e', 'rare', 'r', 'common', 'c']
    classes = ['druid', 'd', 'hunter', 'h', 'mage', 'm',
               'paladin', 'pa', 'priest', 'pr', 'rogue', 'ro',
               'shaman', 's', 'warlock', 'wl', 'warrior', 'wr']

    check_cmd_input()

    chomped = get_file_contents(filename)

    process_input(rarities, classes, chomped)

if __name__ == "__main__":
    main()
