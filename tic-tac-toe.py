import random


def display_board(board):
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')


def player_input():
	marker = ''
	while not (marker == 'X' or marker == 'O'):
		marker = input('Player 1: Do you want to be X or O? ').upper()

	if marker == 'X':
		return 'X', 'O'
	else:
		return 'O', 'X'


def place_marker(board, marker, position):
	board[position] = marker


def win_check(board, marker):
	if (marker == board[1] == board[2] == board[3]) or (marker == board[4] == board[5] == board[6]) or (
			marker == board[7] == board[8] == board[9]):
		return True
	elif (marker == board[1] == board[3] == board[7]) or (marker == board[2] == board[5] == board[8]) or (
			marker == board[3] == board[6] == board[9]):
		return True
	elif (marker == board[1] == board[5] == board[9]) or (marker == board[7] == board[5] == board[3]):
		return True
	else:
		return False


def choose_first():
	if random.randint(1, 2) == 1:
		return "Player 1 first move"
	else:
		return "Player 2 first move"


def space_check(board, position):
	return board[position] == ' '


def player_choice(board):
	position = 0
	while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
		position = int(input('Please enter a number from 1 to 9' + '\n'))

	return position


def full_board_check(board):
	for i in range(1, 10):
		if space_check(board, i):
			return False
	return True


def replay():
	return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
	# Reset the board
	theBoard = [' '] * 10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn + ' will go first.')

	play_game = input('Are you ready to play? Enter Yes or No.')

	if play_game.lower()[0] == 'y':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == 'Player 1':
			# Player1's

			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player1_marker, position)

			if win_check(theBoard, player1_marker):
				display_board(theBoard)
				print('Player 1 has won!')
				game_on = False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('The game is a draw!')
					break
				else:
					turn = 'Player 2'

		else:
			# Player2

			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player2_marker, position)

			if win_check(theBoard, player2_marker):
				display_board(theBoard)
				print('Player 2 has won!')
				game_on = False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('The game is a draw!')
					break
				else:
					turn = 'Player 1'

	if not replay():
		break
