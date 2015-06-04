def get_list(card_file):
    f = open(card_file, 'r')
    card_list = f.readlines()
    f.close()
    return card_list

def get_lists():
    basic = get_list('basic.txt')
    classic = get_list('classic.txt')
    gvg = get_list('gvg.txt')
    naxx = get_list('naxx.txt')
    blackrock = get_list('blackrock.txt')
    reward = get_list('reward.txt')
    promo = get_list('promo.txt')

    return basic, classic, gvg, naxx, blackrock, reward, promo

def get_filter():
    user_filter = input("Pick a filter: Class, Cost, Set, Type, Rarity").lower()

    filters = ['class', 'cost', 'set', 'type', 'rarity']
    if user_filter not in filters:
        print("Filter type invalid.")
        user_filter = get_filter()
    return user_filter

def get_card_lists():
    basic_list, classic_list, gvg_list, 
    naxx_list, blackrock_list, reward_list, promo_list = get_lists()
    card_lists = []
    card_lists.append(basic_list)
    card_lists.append(classic_list)
    card_lists.append(gvg_list)
    card_lists.append(naxx_list)
    card_lists.append(blackrock_list)
    card_lists.append(reward_list)
    card_lists.append(promo_list)
    
    return card_lists

def get_filter_text(filter_type):
    if filter_type == 'class':
        filter_text = get_class()
    elif filter_type == 'cost':
        filter_text = get_cost()
    elif filter_type == 'set':
        filter_text = get_set()
    elif filter_type == 'type':
        filter_text = get_type()
    elif filter_type == 'rarity':
        filter_text = get_rarity()

    return filter_text

def get_class():
    classes = ['driud', 'hunter', 'mage', 'paladin', 'priest', 'rogue', 'shaman', 'warlock', 'warrior']
    chosen_class = input("Which class's cards would you like to view?").lower()
    if chosen_class not in classes:
        print("Class type invalid.")
        chosen_class = get_class()
    return chosen_class

def get_cost():
    costs = []
    costs.extend(range(1,21))
    chosen_cost = input("What cost would you like to look for?")
    if chosen_cost not in costs:
        print("Chosen cost invalid.")
        chosen_cost = get_cost()
    return chosen_cost

def get_set():
    sets = ['basic', 'classic', 'gvg', 'naxx', 'blackrock', 'reward', 'promo']
    chosen_set = input("Which set would you like to see?")
    if chosen_set not in sets:
        print("Chosen set invalid.")
        chosen_set = get_set()
    return chosen_set

def get_type():
    types = ['']

if __name__ == '__main__':
    card_lists = get_card_lists()
    filter_type = get_filter()


