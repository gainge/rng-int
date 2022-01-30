
M = 2**32

def advance_seed(seed):
    return ((seed * 214013) + 2531011) % M


def is_quit(userInput):
    return userInput == 'x' or userInput == 'X'

def get_user_hex(prompt='Please Enter Seed'):
    while True:
        userSeed = input(prompt)
        userSeed = userSeed.replace(' ', '')

        # Return if quit sentinel is entered
        if is_quit(userSeed): return userSeed

        # Otherwise, validate the hex input
        try:
            intVal = int(userSeed, 16)
            return intVal
        except ValueError:
            print()
            print('!----- Please enter a hex value -----!')

#Returns a value between 0 and max_val-1
def get_random_int(seed, max_val):
    # Advance that seed, dog
    seed = advance_seed(seed)

    top_bits = seed // 2**16
    return ((max_val * top_bits) // 2**16), seed

def display_hex_from_int(val):
    hexString = "{0:#0{1}x}".format(val,10).upper()

    return f'0x{hexString[2:]}'

MAX_BUFFER_SIZE = 5
NAME_MAX_VAL = 145
names = [
    'AAAA',
    '1DER',
    '2BIT',
    '2L8',
    '2PAY',
    '401K',
    '4BDN',
    '4BY4',
    '4EVA',
    '7HVN',
    'AOK',
    'ARCH',
    'ARN',
    'ASH',
    'BAST',
    'BBBB',
    'BCUZ',
    'BETA',
    'BOBO',
    'BOMB',
    'BONE',
    'BOO',
    'BORT',
    'BOZO',
    'BUB',
    'BUD',
    'BUZZ',
    'BYRN',
    'CHUM',
    'COOP',
    'CUBE',
    'CUD',
    'DAYZ',
    'DIRT',
    'DIVA',
    'DNCR',
    'DUCK',
    'DUD',
    'DUFF',
    'DV8',
    'ED',
    'ELBO',
    'FAMI',
    'FIDO',
    'FILO',
    'FIRE',
    'FLAV',
    'FLEA',
    'FLYN',
    'GBA',
    'GCN',
    'GLUV',
    'GR8',
    'GRIT',
    'GRRL',
    'GUST',
    'GUT',
    'HAMB',
    'HAND',
    'HELA',
    'HEYU',
    'HI5',
    'HIKU',
    'HOOD',
    'HYDE',
    'IGGY',
    'IKE',
    'IMPA',
    'JAZZ',
    'JEKL',
    'JOJO',
    'JUNK',
    'KEY',
    'KILA',
    'KITY',
    'KLOB',
    'KNEE',
    'L33T',
    'L8ER',
    'LCD',
    'LOKI',
    'LULU',
    'MAC',
    'MAMA',
    'ME',
    'MILO',
    'MIST',
    'MOJO',
    'MOSH',
    'NADA',
    'ZZZZ',
    'NAVI',
    'NELL',
    'NEWT',
    'NOOK',
    'NEWB',
    'ODIN',
    'OLAF',
    'OOPS',
    'OPUS',
    'PAPA',
    'PIT',
    'POP',
    'PKMN',
    'QTPI',
    'RAM',
    'RNDM',
    'ROBN',
    'ROT8',
    'RUTO',
    'SAMI',
    'SET',
    'SETI',
    'SHIG',
    'SK8R',
    'SLIM',
    'SMOK',
    'SNES',
    'SNTA',
    'SPUD',
    'STAR',
    'THOR',
    'THUG',
    'TIRE',
    'TLOZ',
    'TNDO',
    'TOAD',
    'TOMM',
    'UNO',
    'VIVI',
    'WALK',
    'WART',
    'WARZ',
    'WITH',
    'YETI',
    'YNOT',
    'ZAXO',
    'ZETA',
    'ZOD',
    'ZOE',
    'WORM',
    'GEEK',
    'DUDE',
    'WYRN',
    'BLOB'
]

seed = get_user_hex('Please Input Starting Seed: ')
buffer = []

name_index, next_seed = get_random_int(seed, NAME_MAX_VAL)

count = 1
while True:
    # Display results
    print(f'{display_hex_from_int(seed)} => {names[name_index]}', end='')

    # Update buffer and seed
    if len(buffer) >= MAX_BUFFER_SIZE:
        buffer.pop()
    buffer.insert(0, name_index)

    # Wait for user to advance, listen for quit
    user_input = input()

    if is_quit(user_input): break

    # Otherwise, increment the seed and compute the next value
    while True:
        seed = next_seed
        name_index, next_seed = get_random_int(seed, NAME_MAX_VAL)

        # Check for buffer overlap
        if not name_index in buffer: break
