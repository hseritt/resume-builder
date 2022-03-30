#!/usr/bin/env python

import sys

source_file = 'Resume-Builder.txt'
target_file = 'choices.txt'
discarded_file = 'choices-discarded.txt'

debug = True

target_text = ''
discarded_text = ''

try:
    target_text = open(target_file, 'r').read()
except FileNotFoundError as e:
    open(target_file, 'w').close()
    target_text = open(target_file, 'r').read()

try:
    discarded_text = open(discarded_file, 'r').read()
except FileNotFoundError as e:
    open(discarded_file, 'w').close()
    discarded_text = open(discarded_file, 'r').read()

for line in open(source_file, 'r').readlines():
    line = line.rstrip()
    if line not in target_text and line not in discarded_text:
        if line != '' and not line.endswith(':'):
            unanswered = True
            while unanswered:
                if debug:
                    print('-- start --')
                answer = input('\ntext: {}\n\n(Y)es/(N)o/E(x)it > '.format(line))
                if debug:
                    print('-- end --\n\n')

                if answer.lower() == 'y':
                    print('Saving line to {}'.format(target_file))
                    open(target_file, 'a').write(line + '\n')
                    unanswered = False
                elif answer.lower() == 'n':
                    print('Discarding ...')
                    open(discarded_file, 'a').write(line + '\n')
                    unanswered = False
                elif answer.lower() == 'x':
                    print('Quitting ...')
                    sys.exit()
                else:
                    print('\nPlease answer ...\n')
