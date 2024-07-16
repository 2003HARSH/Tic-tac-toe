import myfiglet
import copy

class TicTacToe:

    def __init__(self,level=None) -> None:
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.level=level

    @staticmethod
    def is_board_full(board):
        if ('-' not in board[0] and '-' not in board[1] and '-' not in board[2]):
            return True
        return False

    def show_board(self):   
        print( '-------------------\t\t\t\t-------------------')
        print(f'|  {self.board[0][0]}  |  {self.board[0][1]}  |  {self.board[0][2]}  |\t\t\t\t|  7  |  8  |  9  |')
        print( '|-----|-----|-----|\t\t\t\t-------------------')
        print(f'|  {self.board[1][0]}  |  {self.board[1][1]}  |  {self.board[1][2]}  |\t\t\t\t|  4  |  5  |  6  |')
        print( '|-----|-----|-----|\t\t\t\t-------------------')
        print(f'|  {self.board[2][0]}  |  {self.board[2][1]}  |  {self.board[2][2]}  |\t\t\t\t|  1  |  2  |  3  |')
        print( '-------------------\t\t\t\t-------------------')

    def fill_board(self, x, y, count):
        if self.board[x][y] == '-':
            self.board[x][y] = self.status(count)
        else:
            print("Sorry bro ..you lost your chance.... :(")
            print("Because you entered wrong coordinates....")

    def status(self, count):
        if count % 2 == 0:
            return 'O'
        else:
            return 'X'

    @staticmethod
    def won(board, sym):
        if (board[0] == [sym, sym, sym] or board[1] == [sym, sym, sym]
                or board[2] == [sym, sym, sym]):
            return True
        elif (board[0][0] == sym and board[1][0] == sym
              and board[2][0] == sym):
            return True
        elif (board[0][1] == sym and board[1][1] == sym
              and board[2][1] == sym):
            return True
        elif (board[0][2] == sym and board[1][2] == sym
              and board[2][2] == sym):
            return True
        elif (board[0][0] == sym and board[1][1] == sym
              and board[2][2] == sym):
            return True
        elif (board[0][2] == sym and board[1][1] == sym
              and board[2][0] == sym):
            return True
        else:
            return False

    @staticmethod
    def get_empty_squares(board):
        l=[]
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]=='-':
                    l.append((i,j))
        return l

    def minimax(self,board,maximising):
        if TicTacToe.won(board,"X"):
            return 1,None  #--> eval,move               #user wins
        elif TicTacToe.won(board,"O"):
            return -1,None  #-->eval,Move               computer wins
        elif TicTacToe.is_board_full(board):
            return 0,None #-->eval,Move                 draw
        
        if maximising:
            max_eval=-10
            best_move=None
            empty_squares=TicTacToe.get_empty_squares(board)
            for (row,col) in empty_squares:
                temp_board=copy.deepcopy(board)
                temp_board[row][col]="X"
                eval=self.minimax(temp_board,False)[0]
                if eval>max_eval:
                    max_eval=eval
                    best_move=(row,col) 
            return max_eval,best_move

        elif not maximising:
            min_eval=10
            best_move=None
            empty_squares=TicTacToe.get_empty_squares(board)
            for (row,col) in empty_squares:
                temp_board=copy.deepcopy(board)
                temp_board[row][col]="O"
                eval=self.minimax(temp_board,True)[0]
                if eval<min_eval:
                    min_eval=eval
                    best_move=(row,col) 
            return min_eval,best_move

    def computer_brain(self,count):
        if count==2:
            if self.board[1][1] == 'X':
                self.board[0][0] = 'O'
            else:
                self.board[1][1] = 'O'            
            return    
        elif count == 4 and self.board[1][1] == 'X' and self.board[2][2] == 'X' and self.level<2:
            self.board[1][0] = 'O'
        elif count==4 and self.board[1][1]=='O' and self.board[2][0]=='X' and self.board[0][2]=='X' and self.level<3:
            self.board[0][0]='O'            
        else:
            board=copy.deepcopy(self.board)
            eval,move=self.minimax(board,False)
            self.board[move[0]][move[1]]='O'
            return

    def start_vs_computer(self):
        coor={7:(0,0),8:(0,1),9:(0,2),4:(1,0),5:(1,1),6:(1,2),1:(2,0),2:(2,1),3:(2,2)}
        print("Symbol for User--> 'X' " )
        print("Symbol for Computer--> 'O' " )
        counter=1
        while (not TicTacToe.is_board_full(self.board)):
            self.show_board()
            if counter%2==0:
                print("Computer's turn :")
                self.computer_brain(counter)
            else:
                print("User's turn :")
                num=int(input("Enter the number corresponding to your place :"))
                x,y=coor[num]
                self.fill_board(int(x),int(y),counter)
            if (self.won(self.board,self.status(counter))):
                if counter%2==0:
                    print("Computer has Won..... :")
                    self.show_board()
                    myfiglet.display("You lost",pattern='name',colour='red')
                    return
                else:  
                    print("User has Won..... :")   
                    self.show_board()
                    myfiglet.display("you won",pattern='name',colour='cyan')  
                    return              
            counter+=1
        print("Game is Draw.....")
        self.show_board()    
        myfiglet.display("Draw","!",colour='yellow')

    def start_vs_player(self):
        coor={7:(0,0),8:(0,1),9:(0,2),4:(1,0),5:(1,1),6:(1,2),1:(2,0),2:(2,1),3:(2,2)}
        print("Symbol for Player 1 --> 'X' " )
        print("Symbol for Player 2 --> 'O' " )
        counter=1
        while (not TicTacToe.is_board_full(self.board)):
            self.show_board()
            if counter%2==0:
                print("Player 2's turn :")
            else:
                print("Player 1's turn :")
            print()
            num=int(input("Enter the number corresponding to your place :"))
            x,y=coor[num]
            self.fill_board(int(x),int(y),counter)

            if (TicTacToe.won(self.board,self.status(counter))):
                if counter%2==0:
                    print("Player 2' has Won..... :")
                    myfiglet.display("player 2 won","%",colour='cyan')
                else:
                    print("Player 1' has Won..... :")     
                    myfiglet.display("player 1 won","%",colour='cyan')
                self.show_board()    
                return              
                
            counter+=1
        print("Game is Draw.....") 
        self.show_board()    
        myfiglet.display("Draw","!",colour='yellow')  