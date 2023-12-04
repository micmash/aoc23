games_text = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

r = 12
g = 13
b = 14

def parse_input():
    with open("input_example.txt") as f:
    #with open("input_example_small.txt") as f:
        inp = f.read()
    print(inp)
    games = inp.split('\n')
    return games


class Game:
    def __init__(self, inp):
        init_split = inp.split(':')
        round_split = init_split[1].split(';')
        self.id = init_split[0].split('Game')[1]
        self.blue_max = -1
        self.green_max = -1
        self.red_max = -1
        self.blue_min = 100000000
        self.green_min = 100000000
        self.red_min = 100000000
        self.rounds = round_split
        self.possible = False

    
    def update_max_colors(self):
        for round in self.rounds:
            for color in round.split(','):
                s_color = color.strip().split(' ')
                color_int = int(s_color[0])
                if 'blue' in s_color:
                    if color_int >= self.blue_max:
                        self.blue_max = color_int
                if 'red' in s_color:
                    if color_int >= self.red_max:
                        self.red_max = color_int    
                if 'green' in s_color:
                    if color_int >= self.green_max:
                        self.green_max = color_int

    
    def update_min_colors(self):
        for round in self.rounds:
            for color in round.split(','):
                s_color = color.strip().split(' ')
                color_int = int(s_color[0])
                if 'blue' in s_color:
                    if color_int <= self.blue_min:
                        self.blue_min = color_int
                if 'red' in s_color:
                    if color_int <= self.red_min:
                        self.red_min = color_int    
                if 'green' in s_color:
                    if color_int <= self.green_min:
                        self.green_min = color_int

    def check_if_game_possible(self):
        return self.blue_max <= b and self.green_max <= g and self.red_max <= r
            
        

def main():
    games = parse_input()
    game_list = []
    for game in games:
        game_list.append(Game(game))
    sum = 0
    sum_power = 0
    for i in game_list:
        i.update_max_colors()
        i.update_min_colors()
        print(f"id: {i.id}, blue: {i.blue_max, i.blue_min}, red: {i.red_max, i.red_min}, green: {i.green_max, i.green_min}, power: {i.blue_max*i.red_max*i.green_max}")
        if i.check_if_game_possible():
            print("possible")
            sum+=int(i.id)
        else:
            print('not possible')
        sum_power+=(i.blue_max*i.red_max*i.green_max)
    return sum, sum_power


if __name__ == '__main__':
    print(main())