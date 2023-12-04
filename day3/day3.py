from functools import reduce
from operator import mul
def parse_input():
    with open("/Users/logan.mccamish/day3/day3_example.txt") as f:
    #with open("day3_example_small.txt") as f:
        inp = f.read()
    print(inp)
    games = inp.split('\n')
    return games

class Board():
    def __init__(self, text_board):
        self.max_row = len(text_board)-1
        self.max_column = len(text_board[0])-1
        self.board = [[0] * len(text_board) for _ in range(len(text_board[0]))]
        self.text_board = text_board
        for row in range(0,len(text_board)):
            for column in range(0,len(text_board[0])):
                c = self.text_board[row][column]
                self.board[row][column] = {'c': c, 'processed': False}

    def get_char(self, row, column):
        return self.board[row][column]['c']
    
    def process(self, row, column):
        self.board[row][column]['processed'] = True

    def set_total_number(self, row, column, num):
        self.board[row][column]['total'] = num

    
    def process_board(self):
        for row in range(0, self.max_row+1):
            for column in range(0, self.max_column+1):
                c = self.board[row][column].get('c')
                if c.isdigit() and not self.board[row][column].get('processed'):
                    self.board[row][column]['num'] = self.PartNumber(row, column, board=self)
    
    def scan(self, row, column):
        to_multiply = set()
        if row - 1 >= 0:
            if column -1 >= 0:
                to_multiply.add(self.board[row-1][column-1].get('total'))
            if column + 1 <= self.max_column:
                to_multiply.add(self.board[row-1][column+1].get('total'))
            to_multiply.add(self.board[row-1][column].get('total'))
        if row + 1 <= self.max_row:
            if column -1 >= 0:
                to_multiply.add(self.board[row+1][column-1].get('total'))
            if column + 1 <= self.max_column:
                to_multiply.add(self.board[row+1][column+1].get('total'))
            to_multiply.add(self.board[row+1][column].get('total'))
        if column - 1 >= 0:
            to_multiply.add(self.board[row][column-1].get('total'))
        if column + 1 <= self.max_column:
            to_multiply.add(self.board[row][column+1].get('total'))
        print(to_multiply)
        return to_multiply

        

    class PartNumber():
        def __init__(self, row, column, board):
            self.game_board = board
            self.start_row = row
            self.start_column = column
            self.length = self.get_length()
            self.number = self.get_number()
            self.total_number = self.set_total_number()
            self.surrounding_location = self.get_surrounding_locations()


        def get_length(self):
            length = 0
            column = self.start_column
            while self.game_board.get_char(self.start_row, column).isdigit():
                self.game_board.process(self.start_row, column)
                column += 1
                length += 1
                if column > self.game_board.max_column:
                    return length
            return length
        

        def get_number(self):
            num = 0
            off = 0
            t_length = self.length-1
            while t_length >= 0:
                m = pow(10, t_length)
                num += m*int(self.game_board.get_char(self.start_row, self.start_column+off))
                t_length -= 1
                off += 1
            return num
        
        
        def get_surrounding_locations(self):
            locations = []
            e_column = self.start_column + self.length
            for column_location in range(self.start_column-1, e_column+1):
                if 0 <= column_location <= self.game_board.max_column:
                    if self.start_row-1 >= 0:
                        locations.append({'column': column_location, 'row':self.start_row - 1})
                    locations.append({'column': column_location, 'row':self.start_row})
                    if self.start_row + 1 <= self.game_board.max_row:
                        locations.append({'column': column_location, 'row':self.start_row + 1})
            return locations
        
        def set_total_number(self):
            e_column = self.start_column + self.length
            for column_location in range(self.start_column, e_column):
                self.game_board.set_total_number(self.start_row, column_location, self.number)

        
        def is_part_number(self):
            for loc in self.surrounding_location:
                row = loc['row']
                column = loc['column']
                if not self.game_board.get_char(row,column) == '.' and not self.game_board.get_char(row,column).isdigit():
                    return True
            return False



def main():
    games = parse_input()
    game_board = Board(games)
    game_board.process_board()
    sum = 0
    for r in range(0, len(game_board.board)):
        for c in range(0, len(game_board.board[0])):
            result = 0
            if game_board.get_char(r,c) == '*':
                s = game_board.scan(r, c)
                s.discard(None)
                if len(s) >= 2:
                    result = reduce(mul, s)    
                    print (result)
                    sum+=result
    return sum



if __name__ == '__main__':
    print(main())