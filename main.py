import myfiglet      
from src.tic_tac_toe import TicTacToe

myfiglet.display("welcome to game ", "@", rainbow=True)
print("\nThe placeholders are numbered according to the numeric keys on keyboard : ")
print("Use them to put your mark in the right place:")
print("Enjoy Playing :)\n")
while True:
    print("1 --> to play VS computer ")
    print("2 --> to play Multiplayer ")
    vs=int(input("Enter your choice ..... : "))
    print()
    if vs==1:
        print("1 -> for EASY")
        print("2 -> for MEDIUM")
        print("3 -> for HARD")
        level=int(input("Enter the level of game you wanna play..... : "))
        game = TicTacToe(level)
        myfiglet.display("start", pattern='name', colour='green')
        game.start_vs_computer()
    else:
        game=TicTacToe()
        myfiglet.display("start", pattern='name', colour='green')
        game.start_vs_player()
    choice=input("\n\nPress 'y' to play once again : ")
    if choice not in ['y','Y']:
        break

        
