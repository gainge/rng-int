# Taken from savestate's reddit post explaining Melee's RNG System
# All credit goes to savestate and their hard work!

#@804d5f90
seed = 0x00000001
M = 2**32

#Gets inlined in both functions
#This one is egregious because it ends up being called twice in each
def get_seed():
    global seed
    return seed

#Gets inlined in both functions
#Uses a Linear Congruential Generator with a = 214013, c = 2531011, m = 2**32
#Has a period of 2**32 which is optimal considering the modulus
def next_seed():
    global seed
    seed = ((seed * 214013) + 2531011) % 2**32

def advance_seed(seed):
    return ((seed * 214013) + 2531011) % M

#Returns a value between 0 and max_val-1
def get_random_int(seed, max_val):
    # Advance that seed, dog
    seed = advance_seed(seed)

    top_bits = seed // 2**16
    return ((max_val * top_bits) // 2**16), seed


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

def get_user_input(prompt='Please Enter Value: '):
    while True:
        user_input = input(prompt)

        # Return if quit sentinel is entered
        if is_quit(user_input): return user_input

        # Otherwise, validate integer input
        try:
            intVal = int(user_input)
            return intVal
        except ValueError:
            print()
            print('!----- Please enter an integer value -----!')
            
            

def display_hex_from_int(val):
    hexString = "{0:#0{1}x}".format(val,10).upper()

    return f'0x{hexString[2:]}'


def parse_y_n(answer):
    return (answer == 'y' or answer == 'Y')


is_set_max = input('Use Constant Max Value? (y/n) ')
if parse_y_n(is_set_max):
    max_val = get_user_input('Please Enter Max: ')

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
    'BONE',
    'BOMB?',
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

print()
print('===================')
print('SSBM RNG INT Gaming')
print('===================')

while True:
    print('Please Supply Seed (x to quit)')
    # Grab hex seeds from the user
    seed = get_user_hex('Please Enter Seed: ')
    if is_quit(seed): break

    if not parse_y_n(is_set_max):
        max_val = get_user_input('Please Enter Max: ')
        if is_quit(max_val): break

    print()

    result, next_seed = get_random_int(seed, max_val)

    print(f'Result: {result} ({names[result]})')
    print(f'Result Seed: {display_hex_from_int(next_seed)}')
    print('========================================')

print('Exiting....')


