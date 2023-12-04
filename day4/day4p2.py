def parse_input():
    #with open("day4_input.txt") as f:
    with open("day4_small_input.txt") as f:
        inp = f.read()
    print(inp)
    games = inp.split('\n')
    games2 = []
    for g in games:
        games2.append(g.split(':')[1])
    return games2


class Game():
    def __init__(self, text_board, card_number):
        t = text_board.split('|')
        temp_winning_numbers = t[0][1:].split(' ')
        temp_possible_wins = t[1][1:].split(' ')
        self.winning_numbers = []
        self.possible_wins = []
        self.number = card_number
        for n in temp_winning_numbers:
            if n != '':
                self.winning_numbers.append(n)
        for i in temp_possible_wins:
            if i != '':
                self.possible_wins.append(i)

        print(f'{self.possible_wins}, {self.winning_numbers}')

    def __str__(self):
        return f'{self.winning_numbers} {self.possible_wins}'


class CardList():
    def __init__(self, card_list):
        self.card_list = []
        for card in card_list:
            self.card_list.append({card.number:[card]})
        
    def add_copy(self, card_number):
        self.card_list[card_number].append(self.card_list[card_number][0])

    def get_card(self,card_number):
        return self.card_list[card_number][0]
    
    def get_number_of_cards(self):
        return len(self.card_list)
    
    def __str__(self):
        return f'{self.card_list}'


def process_board(board):
    game_board = board['card']
    win_count = 0
    for possible_win in game_board.possible_wins:
        for winning_number in game_board.winning_numbers:
            if possible_win == winning_number:
                win_count += 1
    return win_count


def main():
    games = parse_input()
    cards = []
    i = 1
    for card in games:
        cards.append(Game(card,i))
        i+=1
    card_list = CardList(cards)
    for c in card_list.card_list:
        for k in c.keys():
            print (f'card_number: {k}, card: {c[k][0]}, copies {len(c[k])}')

    for i in range(1,card_list.get_number_of_cards()+1):
        wins = process_board(card_list.get_card(i+1))
        print(wins)
    
    print(card_list) 
    
            
            

        
            
    

        


if __name__ == '__main__':
    print(main())