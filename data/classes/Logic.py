officers = ['5sGen', '4sGen', '3sGen', '2sGen', '1sGen',
			  'Col', 'LtCol', 'Maj', 'Cap', '1Lt', '2Lt',
			  'Sgt']
	
def update_captured_pieces(board, piece):
	board.captured_pieces.append(piece)
	
def attack_check(board, attacker, defender):
	if defender == None:
		return attacker
	#if piece vs flag, attacking piece wins, even if attacker is a flag.
	if defender.notation == 'flag':
		return attacker
	if attacker.notation == 'flag':
		return defender
	#if same rank, kill both, except for flag vs flag
	if attacker.notation == defender.notation:
		update_captured_pieces(board, attacker)
		update_captured_pieces(board, defender)
		return None
	#if spy
	if attacker.notation == 'spy' and defender.notation == 'pvt':
		update_captured_pieces(board, attacker)
		defender.opponent_guess = ['spy']
		defender.reveal()
		return defender
	if attacker.notation == 'pvt' and defender.notation == 'spy':
		update_captured_pieces(board, defender)
		attacker.opponent_guess = ['spy']
		attacker.reveal()
		return attacker
	if attacker.notation == 'spy':
		guess = ['spy']
		for i in officers:
			if defender.notation == i:
				break
			guess.append(i)
		attacker.opponent_guess = guess
		update_captured_pieces(board, defender)
		return attacker
	elif defender.notation == 'spy':
		guess = ['spy']
		for i in officers:
			if attacker.notation == i:
				break
			guess.append(i)
		defender.opponent_guess = guess
		update_captured_pieces(board, attacker)
		return defender
	#if anything else
	if attacker.notation in officers and defender.notation == 'pvt':
		attacker.opponent_guess = officers
		update_captured_pieces(board, defender)
		return attacker
	if defender.notation in officers and attacker.notation == 'pvt':
		defender.opponent_guess = officers
		update_captured_pieces(board, attacker)
		return defender
	if officers.index(attacker.notation) > officers.index(defender.notation):
		guess = ['spy']
		for i in officers:
			if attacker.notation == i:
				break
			guess.append(i)
		update_captured_pieces(board, attacker)
		return defender
	elif officers.index(attacker.notation) < officers.index(defender.notation):
		guess = ['spy']
		for i in officers:
			if attacker.notation == i:
				break
			guess.append(i)
		update_captured_pieces(board, defender)
		return attacker
