#!/usr/bin/env python

import os
import sys
from positions import positions

source_file = 'choices.txt'

positions_dir = 'positions'

# Clear all position files

for position in positions:
    try:
        open(
            '{}/{}.txt'.format(
                positions_dir, position['id']
            ), 'w'
        ).close()
    except FileNotFoundError as e:
        os.mkdir(positions_dir)
        open(
            '{}/{}.txt'.format(
                positions_dir, position['id']
            ), 'w'
        ).close()

for line in open(source_file, 'r').readlines():
    print('-- start -- ')
    print(line.rstrip())
    print(' Enter a position number that best fits the task')
    for position in positions:
        print(
            'ID: {} Company: {} Position: {}'.format(
                position['id'],
                position['company'],
                position['company']
            )
        )
    print(' Enter x to quit')
    answer = input('>> ')
    print('-- end --\n\n')

    if answer.lower() == 'x':
        print('Exiting ...')
        sys.exit()
    else:
        open('{}/{}.txt'.format(positions_dir, answer), 'a').write(line)
