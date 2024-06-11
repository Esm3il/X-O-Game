import Player
import math
import random
import time



class TikTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for i in range(9)] #[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        nums_board = [str(i) for i in range(9)]
        for row in [nums_board[i*3:(i+1) * 3]for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print('')

    def winner(self, square , letter):
        row_inx = math.floor(square/3)
        row = self.board[row_inx*3 : (row_inx + 1)*3]

        if all(s == letter for s in row):
            return True
        
        col_inx = square % 3
        col = [self.board[col_inx + i*3] for i in range(3)]
        if all(s == letter for s in col):
            return True
        
        if square%2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all(s==letter for s in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all(s==letter for s in diagonal2):
                return True
        return False
        # elif((self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[0] != ' ') or
        #      (self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[2] != ' ')):
        #     return True
        # return False

    def make_move(self, square , letter):
        if(self.board[square] == ' '):
            self.board[square] = letter
            if(self.winner(square , letter) == True):
                self.current_winner = letter
            return True
        return False


    #check of there is empty squares in board
    def empty_squares(self):
        return ' ' in self.board
    
    #return number of empty squares
    def num_empty_squares(self):
        return self.board.count(' ')
    
    #return number of available moves
    def available_moves(self):
        return [i for i,x in enumerate(self.board) if x==' ']

    

def play(game, x_player , o_player , print_game=True):

    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if(print_game):
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!')
                    break
            letter = 'O' if letter=='X' else 'X'
        time.sleep(.3)
        print(game.empty_squares())
    if ((game.num_empty_squares() == 0) and (game.current_winner == None)):
        print('It\'s a tie')



x_player = Player.HumanPlayer('X')
o_player = Player.IntelligentComputerPlayer('O')
t = TikTacToe()
play(t , x_player , o_player)