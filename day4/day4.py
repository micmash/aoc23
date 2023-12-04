def parse_input():
    with open("day4_input.txt") as f:
    #with open("day4_small_input.txt") as f:
        inp = f.read()
    print(inp)
    games = inp.split('\n')
    games2 = []
    for g in games:
        games2.append(g.split(':')[1])
    return games2


class Game():
    def __init__(self, text_board):
        t = text_board.split('|')
        temp_winning_numbers = t[0][1:].split(' ')
        temp_possible_wins = t[1][1:].split(' ')
        self.winning_numbers = []
        self.possible_wins = []
        for n in temp_winning_numbers:
            if n != '':
                self.winning_numbers.append(n)
        for i in temp_possible_wins:
            if i != '':
                self.possible_wins.append(i)

        print(f'{self.possible_wins}, {self.winning_numbers}')

def main():
    games = parse_input()
    boards = []
    num = 1
    for g in games:
        boards.append({'card_number': num, 'game': Game(g)})
        num += 1
    sum = 0
    for b in boards:
        p = 0
        for possible_win in b['game'].possible_wins:
            for winning_number in b['game'].winning_numbers:
                if possible_win == winning_number:
                    print(f'found win: {winning_number, possible_win}')
                    p += 1
        print('next_board')
        if p > 0:
            sum += pow(2,(p-1))
    print(sum)

        


if __name__ == '__main__':
    print(main())