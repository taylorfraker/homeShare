# Interest Calculator


def compound(r, n, t, p):
	answer = (p * (1 + r / n) ** (n * t))
	print('Wow! By then you\'ll have $' + str(answer))

prompt = 'not q'

while prompt != 'q':
	deposit = int(input('Welcome to the Bank of Python! How much would you like to deposit today?\n'))
	years = int(input('Excellent! Our interst rate is 5%, which is compunded monthly. How many years would you like to leave your money here?\n'))
	compound(0.05, 12, years, deposit)
	prompt = input('\nPress ENTER to restart.\nType q + ENTER to quit\n')