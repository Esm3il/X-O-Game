import math
import random


class player:
    def __init__(self,letter):
        self.letter = letter
    def get_move(self, game):
        pass

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn.\n Input a number(0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square. Try Again')
        return val    


class IntelligentComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if (len(game.available_moves()) == 9):
            square = random.choice(game.available_moves())
        else:
            square = self.minmax(game, self.letter)['position']
        return square
    
    def minmax(self , state , player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        if state.current_winner == other_player:
            return {'position':None ,'score':1 * (state.num_empty_squares() + 1) if other_player==max_player else -1*(state.num_empty_squares()+1)}
        elif not state.empty_squares():
            return{'Position':None,'score':0}
        
        if player == max_player:
            best = {'position':None , 'score': -math.inf}
        else:
            best = {'position':None , 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            simulate_score = self.minmax(state , other_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            simulate_score['position'] = possible_move

            if player == max_player:
                if simulate_score['score'] > best['score']:
                    best = simulate_score
            
            else:
                if simulate_score['score'] < best['score']:
                    best = simulate_score

        return best