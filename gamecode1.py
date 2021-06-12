
player_x = input("Player X, enter your name: ")
print("Welcome, " + player_x)

player_o = input("Player O, please enter your name: ")
print("Welcome, " + player_o)



board = {1 : "   ", 2 : "   ", 3 : "   ", 4 : "   ", 5 : "   ",\
	 6 : "   ", 7 : "   ", 8 : "   ", 9 : "   ", 10 : "   ",\
	 11 : "   ", 12 : "   ", 13 : "   ", 14 : "   ", 15 : "   ",\
	 16 : "   ", 17 : "   ", 18 : "   ", 19 : "   ", 20 : "   ",\
	 21 : "   ", 22 : "   ", 23 : "   ", 24 : "   ", 25 : "   "}



def print_board():
	print("  - + - + - + - + - +")
	print("|" + board[1] + "|" + board[2] + "|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
	print("  - + - + - + - + - +")
	print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|" + board[9] + "|" + board[10] + "|")
	print("  - + - + - + - + - +")
	print("|" + board[11] + "|" + board[12] + "|" + board[13] + "|" + board[14] + "|" + board[15] + "|")
	print("  - + - + - + - + - +")
	print("|" + board[16] + "|" + board[17] + "|" + board[18] + "|" + board[19] + "|" + board[20] + "|")
	print("  - + - + - + - + - +")
	print("|" + board[21] + "|" + board[22] + "|" + board[23] + "|" + board[24] + "|" + board[25] + "|")
	print("  - + - + - + - + - +")


print_board()


def get_x_move():
	try:
		x_move = int(input(player_x + ", please enter your move: "))
		if not(x_move in range(1, 26)):
			print("Invalid move.")
			return 0
		elif board[x_move] == " B ":
			print("Square is bombed out - please select another square.")
			return 0
		elif (board[x_move] == " X ") or (board[x_move] == " O "):
			print("Square is already occupied - please select another square.") 
			return 0
		else:
			return x_move
	except:
		print("Invalid move.")
		return 0
			
	

def get_o_move():
	try:
		o_move = int(input(player_o + ", please enter your move: "))
		if not(o_move in range(1, 26)):
			print("Invalid move.")
			return 0
		elif board[o_move] == " B ":
			print("Square is bombed out - please select another square.")
			return 0
		elif (board[o_move] == " X ") or (board[o_move] == " O "):
			print("Square is already occupied - please select another square.") 
			return 0
		else:
			return o_move
	except:
		print("Invalid move.")
		return 0




def board_update(x_move, o_move):
	if x_move == o_move:
		board[x_move] = " B "
		square1 = board[1]
		for i in range(1, 17, 5):
			board[i] = board[i + 5]
		for i in range(21, 25):
			board[i] = board[i + 1]
		for i in range(25, 9, -5):
			board[i] = board[i - 5]
		for i in range(5, 2, -1):
			board[i] = board[i - 1]
		board[2] = square1
		return True
	else:
		board[x_move] = " X "
		board[o_move] = " O "

def check_for_winner():
	winner = ""
	winner_count = 0
	if (board[7] == board[8] == board[9] == " X ") or (board[12] == board[13] == board[14] == " X ") or (board[17] == board[18] == board[19] == " X ")\
	 or (board[7] == board[12] == board[17] == " X ") or (board[8] == board[13] == board[18] == " X ") or (board[9] == board[14] == board[19] == " X ")\
	 or (board[7] == board[13] == board[19] == " X ") or (board[9] == board[13] == board[17] == " X ") or (board[2] == board[8] == board[14] == board[20] == " X ")\
	 or (board[6] == board[12] == board[18] == board[24] == " X ") or (board[4] == board[8] == board[12] == board[16] == " X ") or (board[10] == board[14] == board[18] == board[22] == " X ")\
	 or (board[1] == board[2] == board[3] == board[4] == board[5] == " X ") or (board[1] == board[6] == board[11] == board[16] == board[21] == " X ")\
	 or (board[5] == board[10] == board[15] == board[20] == board[25] == " X ") or (board[21] == board[22] == board[23] == board[24] == board[25] == " X "):
		winner += player_x
		winner_count += 1
	if (board[7] == board[8] == board[9] == " O ") or (board[12] == board[13] == board[14] == " O ") or (board[17] == board[18] == board[19] == " O ")\
	 or (board[7] == board[12] == board[17] == " O ") or (board[8] == board[13] == board[18] == " O ") or (board[9] == board[14] == board[19] == " O ")\
	 or (board[7] == board[13] == board[19] == " O ") or (board[9] == board[13] == board[17] == " X ") or (board[2] == board[8] == board[14] == board[20] == " X ")\
	 or (board[6] == board[12] == board[18] == board[24] == " O ") or (board[4] == board[8] == board[12] == board[16] == " O ") or (board[10] == board[14] == board[18] == board[22] == " O ")\
	 or (board[1] == board[2] == board[3] == board[4] == board[5] == " O ") or (board[1] == board[6] == board[11] == board[16] == board[21] == " O ")\
	 or (board[5] == board[10] == board[15] == board[20] == board[25] == " O ") or (board[21] == board[22] == board[23] == board[24] == board[25] == " O "):
		winner += player_o
		winner_count += 1
	if winner_count == 1:
		print(winner + " has won the game.")
		return winner_count
	else: 
		return winner_count
		


def full_board():
	if list(board.values()).count("   ") == 0:
		for i in (7, 8, 9, 12, 13, 14, 17, 18, 19):
			board[i] = "   "



def play_a_game():
	game_done = False
	while game_done == False:
		x_move = 0
		while x_move == 0:
			x_move += get_x_move()
		o_move = 0
		while o_move == 0:
			o_move += get_o_move()
		bomb_test = board_update(x_move, o_move)
		win_check = check_for_winner()
		if win_check == 1:
			game_done = True
		elif win_check == 2: 
			board[x_move] = " B "
			board[o_move] = " B "
			full_board()
		elif not(bomb_test or (win_check == 1) or (win_check == 2)):
			for i, j in board.items():
				if j == " B ":
					board[i] = "   "
			full_board()
		else:
			full_board()
		print_board()
	
play_a_game()


	
		
		
	


	




