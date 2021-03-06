#!/usr/bin/env python3
import sys
import random

class Settings(object):
    def __init__(self):
        self.timebank = None 
        self.time_per_move = None
        self.player_names = None 
        self.your_bot = None
        self.your_botid = None
        self.field_width = None
        self.field_height = None


class Field(object):
    def __init__(self):
        self.field_state = None

    def update_field(self, celltypes, settings):
        self.field_state = [[] for _ in range(settings.field_height)]
        n_cols = settings.field_width
        for idx, cell in enumerate(celltypes):
            row_idx = idx // n_cols
            self.field_state[row_idx].append(cell)


class State(object):
    def __init__(self):
        self.settings = Settings()
        self.field = Field()
        self.round = 0


def parse_communication(text):
    """ Return the first word of the communication - that's the command """
    return text.strip().split()[0] 


def settings(text, state):
    """ Handle communication intended to update game settings """
    tokens = text.strip().split()[1:] # Ignore token 0, it's the string "settings".
    cmd = tokens[0]
    if cmd in ('timebank', 'time_per_move', 'your_botid', 'field_height', 'field_width'):
        # Handle setting integer settings.
        setattr(state.settings, cmd, int(tokens[1]))
    elif cmd in ('your_bot',):
        # Handle setting string settings.
        setattr(state.settings, cmd, tokens[1])
    elif cmd in ('player_names',):
        # Handle setting lists of strings.
        setattr(state.settings, cmd, tokens[1:])
    else:
        raise NotImplementedError('Settings command "{}" not recognized'.format(text))
    

def update(text, state):
    """ Handle communication intended to update the game """
    tokens = text.strip().split()[2:] # Ignore tokens 0 and 1, those are "update" and "game" respectively.
    cmd = tokens[0]
    if cmd in ('round',):
        # Handle setting integer settings.
        setattr(state.settings, 'round', int(tokens[1]))
    if cmd in ('field',):
        # Handle setting the game board.
        celltypes = tokens[1].split(',')
        state.field.update_field(celltypes, state.settings)


def action(text, state):
    """ Handle communication intended to prompt the bot to take an action """
    tokens = text.strip().split()[1:] # Ignore token 0, it's the string "action".
    cmd = tokens[0]
    if cmd in ('move',):
        return make_move(state)
    else:
        raise NotImplementedError('Action command "{}" not recognized'.format(text))


def make_move(state):

    # TODO: Implement bot logic here
    rand_col = random.randint(0, state.settings.field_width-1)

    return 'place_disc {}'.format(rand_col)

def main():
    command_lookup = { 'settings': settings, 'update': update, 'action': action }
    state = State() 
    for input_msg in sys.stdin:
        cmd_type = parse_communication(input_msg)
        command = command_lookup[cmd_type]

        # Call the correct command. 
        res = command(input_msg, state)

        # Assume if the command generates a string as output, that we need 
        # to "respond" by printing it to stdout.
        if isinstance(res, str):
            print(res)
            sys.stdout.flush()
        


if __name__ == '__main__':
    main()
