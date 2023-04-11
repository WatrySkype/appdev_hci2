ranked_piece = ['5sGen', '4sGen', '3sGen', '2sGen', '1sGen',
              'Col', 'LtCol', 'Maj', 'Cap', '1Lt', '2Lt',
              'Sgt']

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
        return defender
    if attacker.notation == 'pvt' and defender.notation == 'spy':
        return attacker
    if attacker.notation == 'spy':
        return attacker
    elif defender.notation == 'spy':
        return defender
    #if anything else
    if attacker.notation in ranked_piece and defender.notation == 'pvt':
        return attacker
    if defender.notation in ranked_piece and attacker.notation == 'pvt':
        return defender
    if ranked_piece.index(attacker.notation) > ranked_piece.index(defender.notation):
        return defender
    elif ranked_piece.index(attacker.notation) < ranked_piece.index(defender.notation):
        return attacker