# walk = ['n','s','n','s','n','s','n','s','n','s']
# walk = ['e', 's', 'e', 'n', 'n', 's', 's', 'w', 'n', 'e']
# walk = ['n', 's', 'e', 'e', 'e', 'n', 'n', 's', 'e', 's']
# walk = ['s', 'e', 'e', 'n', 'n', 'w', 'w', 'e', 's', 'e']
# walk = ['e', 's', 's', 's', 's', 'e', 'n', 'n', 'n', 'n']
walk = ['w', 'w', 'w', 'e', 'e', 'e', 'e', 'e', 'w', 'w']
def is_valid_walk(walk):
    if len(walk) == 10:
        if (all(x in walk for x in ['n', 's'])) and (all(x in walk for x in ['e', 'w'])):
            if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'):
                return True
            else:
                return False
        elif 'n' in walk and 's' in walk and 'e' in walk and 'w' in walk:
            if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'):
                return True
            else:
                return False
        elif 'n' in walk and 's' in walk and 'w' not in walk and 'e' not in walk:
            if walk.count('n') == walk.count('s'):
                return True
            else:
                return False
        else:
            if walk.count('e') == walk.count('w'):
                return True
            else:
                return False
    else:
        return False

is_valid_walk(walk)

