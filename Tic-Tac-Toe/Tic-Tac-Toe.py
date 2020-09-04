flag = -1

ceil = [[' ', ' ', ' '],
		[' ', ' ', ' '],
		[' ', ' ', ' ']]


def print_board(ceil):
	print("---------")
	print('| {} {} {} |'.format(ceil[0][0], ceil[0][1], ceil[0][2]))
	print('| {} {} {} |'.format(ceil[1][0], ceil[1][1], ceil[1][2]))
	print('| {} {} {} |'.format(ceil[2][0], ceil[2][1], ceil[2][2]))
	print("---------")


def play_game():
	while True:
		cordinate = input("Enter the coordinates: ").split()
		if check_input(cordinate) == -1:
			continue
		cordinate = list(map(int, cordinate))
		if check_ceil(cordinate) == -1:
			continue
		print_board(ceil)
		if imposible() != 0:
			print(imposible())
			break
		elif wins(ceil) != 0:
			print(wins(ceil))
			break
		elif wins(ceil) == 0 and draw() != 0:
			print(draw())
			break


def check_ceil(cordinate):
	global flag
	x, y = 0, 0
	if cordinate == [1, 1]:
		x, y = 2, 0
	elif cordinate == [1, 2]:
		x, y = 1, 0
	elif cordinate == [1, 3]:
		x, y = 0, 0
	elif cordinate == [2, 1]:
		x, y = 2, 1
	elif cordinate == [2, 2]:
		x, y = 1, 1
	elif cordinate == [2, 3]:
		x, y = 0, 1
	elif cordinate == [3, 1]:
		x, y = 2, 2
	elif cordinate == [3, 2]:
		x, y = 1, 2
	elif cordinate == [3, 3]:
		x, y = 0, 2
	elif ceil[x][y] != ' ':
		print("This cell is occupied! Choose another one!")
		return -1
	if flag == -1:
		ceil[x][y] = "X"
	else:
		ceil[x][y] = "O"
	flag = -flag


def check_input(cordinates):
	for i in cordinates:
		if not i.isdigit():
			print("You should enter numbers!")
			return -1
		elif int(i) not in range(1, 4):
			print("Coordinates should be from 1 to 3!")
			return -1


def draw():
	count = 0
	for i in ceil:
		for j in i:
			if j == ' ':
				count += 1
	if count == 0:
		return "Draw"
	return 0


def wins(ceil):
	for i in range(0, 3):
		if ceil[i][0] == ceil[i][1] == ceil[i][2]:
			if ceil[i][0] != ' ':
				return f'{ceil[i][0]} wins'
		if ceil[0][i] == ceil[1][i] == ceil[2][i]:
			if ceil[0][i] != ' ':
				return f'{ceil[0][i]} wins'
		if ceil[0][0] == ceil[1][1] == ceil[2][2]:
			if ceil[0][0] != ' ':
				return f'{ceil[0][0]} wins'
		if ceil[0][2] == ceil[1][1] == ceil[2][0]:
			if ceil[0][2] != ' ':
				return f'{ceil[0][0]} wins'
	return 0


def imposible():
	x_count = 0
	o_count = 0
	for i in ceil:
		for j in i:
			if j == "X":
				x_count += 1
			if j == "O":
				o_count += 1
	if abs(x_count - o_count) >= 2:
		return "Impossible"
	winner_counter = 0
	for i in range(0, 3):
		if ceil[i][0] == ceil[i][1] == ceil[i][2]:
			if ceil[i][0] != ' ':
				winner_counter += 1
		elif ceil[0][i] == ceil[1][i] == ceil[2][i]:
			if ceil[0][i] != ' ':
				winner_counter += 1
		if winner_counter > 1:
			return "Impossible"
	return 0


print_board(ceil)
play_game()