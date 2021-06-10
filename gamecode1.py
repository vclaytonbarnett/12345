print("Hello, and welcome to 12345. This is similar to a game of tic-tac-toe. You will play on a five by five board. Each spot on the\
 board is mapped by a number. The top left corner is 1. The top row from left to right is 1 2 3 4 5.\
 The second row is 6 7 8 9 10. The third row follows the same pattern.\
 There are multiple ways to win: you can get 3 in a row (diagonals included) in the middle 3 by 3 board, \
 you can get four in a row along a diagonal, or you can get five in a row in any direction.\
 Both players will move at the same time. If both players move to the same spot, that location becomes bombed.\
 A bombed location is empty and cannot be moved to on the next turn. If both players win at the same time,\
 the squares they played on last, to win, both become bombed. Bombed locations\
 remain bombed until a move occurs that doesn't result in bombing. When both players win simultaneously,\
 the exterior pieces (those around the middle 3 by 3 board) rotate one square clockwise.\
 One final catch - if neither player is able to move (if the board is full or bombed-out),\
 all of the pieces in the middle 3 by 3 board will disappear.")

player_x = input("Player x, enter your name: ")
print("Welcome, " + player_x)

player_o = input("Player o, please enter your name: ")
print("Welcome, " + player_o)

x_2move_count = 4
o_2move_count = 4

def get_x_move():
	try:
		x_move = int(input(player_x + ", enter your move: "))
		if not(x_move in range(1, 26)):
			print("Invalid move.")
			get_x_move()
		else:
			return x_move
	except:
		print("Invalid move.")
		get_x_move()
	

def get_o_move():
	try:
		o_move = int(input(player_o + ", enter your move: "))
		if not(o_move in range(1, 26)):
			print("Invalid move.")
		else:
			return o_move
	except:
		print("Invalid move.")


get_x_move()



board = {1 : "-", 2 : "-", 3 : "-", 4 : "-", 5 : " - ",\
	 6 : "-", 7 : "-", 8 : "-", 9 : "-", 10 : " - ",\
	 11 : "-", 12 : "-", 13 : "-", 14 : "-", 15 : " - ",\
	 16 : "-", 17 : "-", 18 : "-", 19 : "-", 20 : " - ",\
	 21 : "-", 22 : "-", 23 : "-", 24 : "-", 25 : " - "}


	



	
