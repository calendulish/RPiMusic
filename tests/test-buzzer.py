#!/usr/bin/env python

import sys
sys.path.append('..')

import RPiMusic

pMusic = RPiMusic.Melody()

try:
    pMusic.buzzerPlay('do-re-mi-fa')
    pMusic.end()
except ImportError as e:
    print(f'Melody {str(e)[17:-1]} not found')
