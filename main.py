from bs4 import BeautifulSoup

class Card:
    def __init__(self, name, power, power_type, effect):
        self.name = name,
        self.power = power,
        self.power_type = power_type,
        self.effect = effect

    def display_card(self):
        print(f'Name: {self.name}. Power: {self.power}. Type: {self.power_type}. Effect: {self.effect}.')


class Player:
    def __init__(self, pName, pPoints, pCards):
        self.pName = pName,
        self.pPoints = pPoints,
        self.pCards = pCards

complete_card_list = []

def populate_cards_list(cardsList):
    global complete_card_list
    for card in cardsList:
        temp = Card(card[0], card[1], card[2], card[3])
        complete_card_list.append(temp)

def displayCompleteCardList():
    for card in complete_card_list:
        card.display_card()

def main():
    with open("./gwentFile.html") as html:
        soup = BeautifulSoup(html, 'html.parser')

    for character in soup.find_all('a', {'class': 'a-link'}):
        charData = []
        #IF <a> tag is a character
        if character.find('img'):
            #Save character name to list
            charData.append(character.text)

            #Power amount
            power = character.find_next("td")

            #Siege Unit, Close combat unit, archery unit
            power_type = power.find_next("td")

            charData.append(power.text)
            charData.append(power_type.text)

            #Get next <a> tag
            nextChar = character.find_next("a")
            #Pass if it is another character.
            if nextChar.find('img'):
                pass
            else:
                #If it is an special ability, save it to the list
                charData.append(nextChar.text)

        
        #print(charData)
        populate_cards_list(charData)

    displayCompleteCardList()

if __name__ == "__main__":
    main()
