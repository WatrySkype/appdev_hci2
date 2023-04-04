from random import choice

def randomize_placement(color):
    pieces = ['5sGen', '4sGen', '3sGen', '2sGen', '1sGen',
              'Col', 'LtCol', 'Maj', 'Cap', '1Lt', '2Lt',
              'Sgt', 'pvt', 'pvt', 'pvt', 'pvt', 'pvt', 'pvt',
              'spy', 'spy', 'flag', '', '', '', '', '', '']
    result = []
    for row in range(3):
        row = []
        for column in range(9):
            random_piece = choice(pieces)
            pieces.remove(random_piece)
            if random_piece != '':
                random_piece = color+random_piece
            row.append(random_piece)         
        result.append(row)
    return result

def colorize(placement, color):
    for row in placement:
        for piece in row:
            if piece == '':
                continue
            piece = color+piece

def randomize_board():
    white_side = randomize_placement('w')
    black_side = randomize_placement('b')
    neutral_side = [['','','','','','','','',''],
            ['','','','','','','','','']]
    white_side.extend(neutral_side)
    white_side.extend(black_side)
    return white_side

print (randomize_board())