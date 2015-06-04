from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import re
import time

def skip_narrow(tag):
    return not tag.startswith('narrowonly')

def scrape_list(url, card_file):
    gvg_url = "http://hearthstone.gamepedia.com/Goblins_vs_Gnomes_card_list"
    naxx_url = "http://hearthstone.gamepedia.com/Naxxramas_card_list"
    reward_url = "http://hearthstone.gamepedia.com/Reward_card_list"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    if url == naxx_url:
        html = str(html).strip()
        html = html.replace("<b>", "")
        html = html.replace("</b>", "")
    soup = BeautifulSoup(html)
    if url == gvg_url or url == naxx_url or url == reward_url:
        table = soup.find('div', id="mw-content-text").find('table', 
            attrs={'class': "wikitable sortable cardtable cardtable-collapsible"})
    else:
        table = soup.find('div', id="mw-content-text").find('table', 
            attrs={'class': "wikitable sortable cardtable cardtable-collapsible cardtable-collapsed"})

    rows = table.find_all('tr')
    rows.pop(0)
    rows.pop()
    count = 0
    for row in rows:
        if not 'class' in row.attrs or row.attrs['class'] != ['narrowonly']:
            card_file.write('Card ' + str(count+1) + ": ")
            cols = row.find_all('td')
            if 'wideonly' in cols[0]['class']:
                name = cols[0].find('a').text
                rarity = cols[2].find('span').findNextSibling('span').text
                card_type = cols[3].text
                card_class = cols[5].find('span').find('span').text
                cost = cols[6].text
                output = []

                name = name.strip().replace('\\n', '').replace('\\', '')
                rarity = rarity.strip().replace('\\n', '').replace('\\', '')
                card_type = card_type.strip().replace('\\n', '').replace('\\', '')
                card_class = card_class.strip().replace('\\n', '').replace('\\', '')
                cost = cost.split()[0]

                output.append(name)
                output.append(rarity)
                output.append(card_type)
                output.append(card_class)
                output.append(cost)
                for item in output:
                    if '\n' in item:
                        item = item[:-2]
                card_file.write(output[0] + ' ' + output[1] + ' ' + output[2] + ' ' + \
                                output[3] + ' ' + output[4])
                card_file.write('\n')

            cols.clear()
            count += 1
    print(count)

if __name__ == "__main__":
    basic_url = "http://hearthstone.gamepedia.com/Basic_card_list"
    classic_url = "http://hearthstone.gamepedia.com/Classic_card_list"
    gvg_url = "http://hearthstone.gamepedia.com/Goblins_vs_Gnomes_card_list"
    naxx_url = "http://hearthstone.gamepedia.com/Naxxramas_card_list"
    blackrock_url = "http://hearthstone.gamepedia.com/Blackrock_Mountain_card_list"
    reward_url = "http://hearthstone.gamepedia.com/Reward_card_list"
    promo_url = "http://hearthstone.gamepedia.com/Promo_card_list"

    basic_file = open('basic.txt', 'w')
    scrape_list(basic_url, basic_file)
    basic_file.close()

    time.sleep(10)

    classic_file = open('classic.txt', 'w')
    scrape_list(classic_url, classic_file)
    classic_file.close()

    time.sleep(10)

    gvg_file = open('gvg.txt', 'w')
    scrape_list(gvg_url, gvg_file)
    gvg_file.close()

    time.sleep(10)

    naxx_file = open('naxx.txt', 'w')
    scrape_list(naxx_url, naxx_file)
    naxx_file.close()

    time.sleep(10)

    blackrock_file = open('blackrock.txt', 'w')
    scrape_list(blackrock_url, blackrock_file)
    blackrock_file.close()

    time.sleep(10)
    
    reward_file = open('reward.txt', 'w')
    scrape_list(reward_url, reward_file)
    reward_file.close()

    time.sleep(10)

    promo_file = open('promo.txt', 'w')
    scrape_list(promo_url, promo_file)
    promo_file.close()
