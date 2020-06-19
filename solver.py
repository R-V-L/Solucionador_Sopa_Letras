__author__ = 'Ricardo Vazquez'

with open('set.txt', 'r') as f:
    solutions = [line.strip().upper() for line in f]

with open('puzzle.txt', 'r') as file:
    puzzle = file.read()

wordgrid = puzzle.replace(' ','')
length = wordgrid.index('\n') + 1

characters = [(letter, divmod(index, length)) for  index, letter in enumerate (wordgrid)]

wordlines = {}
# These next lines just  directions so you can tell which direction the word is going
directions = {'🡣':0, '🡧':-1, '🡦':1}

for word_direction, directions in directions.items():
    wordlines[word_direction] = []
    for x in range(length):
        for i in range(x, len(characters), length + directions):
            wordlines[word_direction].append(characters[i])
        wordlines[word_direction].append('\n')

wordlines['🡢'] = characters
wordlines['🡠'] = [i for i in reversed(characters)]
wordlines['🡡'] = [i for i in reversed(wordlines['🡣'])]
wordlines['🡤'] = [i for i in reversed(wordlines['🡦'])]
wordlines['🡥'] = [i for i in reversed(wordlines['🡧'])]

def sopa(direction, tuple, lines):
    for direction, tuple in lines.items():
        string = ''.join([i[0] for i in tuple])
        for word in solutions:
            if word in string:
                coordinates = tuple[string.index(word)][1]
                print(f'[{word}] esta en Fila [{coordinates[0]+1}], y Columna [{coordinates[1]+1}] en direccion: [{direction}]')

print(f'Sopa de letras:\n\n{puzzle}\n')
sopa(word_direction, tuple, wordlines)