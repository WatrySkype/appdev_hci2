ranked_piece = ['5sGen', '4sGen', '3sGen', '2sGen', '1sGen',
              'Col', 'LtCol', 'Maj', 'Cap', '1Lt', '2Lt',
              'Sgt']

ranking = {
    'pvt' : 0,
    'spy' : 1,
    'Sgt' : 2,
    '2Lt' : 3,
    '1Lt' : 4,
    'Cap' : 5,
    'Maj' : 6,
    'LtCol' : 7,
    'Col' : 8,
    '1sGen' : 9,
    '2sGen' : 10,
    '3sGen' : 11,
    '4sGen' : 12,
    '5sGen' : 13,
    'flag' : 14
    }
def get_rank(a):
    rev = {v:k for k,v in ranking.items()}
    return rev[a]
def attack_check(attacker, defender):
    if defender == None:
        return attacker
    #if piece vs flag, attacking piece wins, even if attacker is a flag.
    if defender.notation == 'flag':
        return attacker
    #if same rank, kill both, except for flag vs flag
    if attacker.notation == defender.notation:
        return None
    #if spy
    if attacker.notation == 'spy' and defender.notation == 'pvt':
        defender.opponent_guess = [0]
        return defender
    if attacker.notation == 'pvt' and defender.notation == 'spy':
        attacker.opponent_guess = [0]
        return attacker
    if attacker.notation == 'spy':
        attacker.opponent_guess = [1]
        return attacker
    elif defender.notation == 'spy':
        defender.opponent_guess = [1]
        return defender
    #if anything else
    if attacker.notation in ranked_piece and defender.notation == 'pvt':
        if ranking[defender.notation] in attacker.opponent_guess:
            attacker.opponent_guess.remove(0)
            attacker.opponent_guess.remove(1)
            attacker.opponent_guess.remove(14)
        return attacker
    if defender.notation in ranked_piece and attacker.notation == 'pvt':
        if ranking[attacker.notation] in defender.opponent_guess:
            defender.opponent_guess.remove(0)
            defender.opponent_guess.remove(1)
            defender.opponent_guess.remove(14)
        return defender
    if ranked_piece.index(attacker.notation) > ranked_piece.index(defender.notation):
        if ranking[attacker.notation] in defender.opponent_guess:
            for x in range(ranking[attacker.notation]+1):
                if x == 1:
                    continue
                defender.opponent_guess.remove(x)
            defender.opponent_guess.remove(14)
        return defender
    elif ranked_piece.index(attacker.notation) < ranked_piece.index(defender.notation):
        if ranking[defender.notation] in attacker.opponent_guess:
            for x in range(ranking[defender.notation]+1):
                if x == 1:
                    continue
                attacker.opponent_guess.remove(x)
            attacker.opponent_guess.remove(14)
        return attacker