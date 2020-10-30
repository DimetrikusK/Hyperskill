def chek_language(my, too):
    if my == 1:
        my = 'arabic'
    elif my == 2:
        my = 'german'
    elif my == 3:
        my = 'english'
    elif my == 4:
        my = 'spanish'
    elif my == 5:
        my = 'french'
    elif my == 6:
        my = 'hebrew'
    elif my == 7:
        my = 'japanese'
    elif my == 8:
        my = 'dutch'
    elif my == 9:
        my = 'polish'
    elif my == 10:
        my = 'portuguese'
    elif my == 11:
        my = 'romanian'
    elif my == 12:
        my = 'russian'
    elif my == 13:
        my = 'turkish'

world_lenguage = ('', 'arabic', 'german', 'english', 'spanish',
                  'french', 'hebrew', 'japanese', 'dutch', 'polish',
                  'portuguese', 'romanian', 'russian', 'turkish')
print(world_lenguage[4].title())