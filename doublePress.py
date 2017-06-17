#!/usr/bin/python

import rx # Could do more qualified import here

from rx              import Observable, Observer
from pykeyboard      import PyKeyboard
from i3CurrentWindow import i3CurrentWindow
from serialToKey     import _keyPresses
from keyConfigs      import keyConfigs

pk = PyKeyboard()

def mapToKey( keyMap, keyList ):
    return keyList[keyMap]

# This is gross! *Continue Refactor*
def mapToPress(mapped):
    newBinding = mapped['window']
    pressed = mapToKey(mapped['keys'], newBinding)

    for keySet in newBinding:
        if keySet['bn'] != ['']:
            if keySet['bn'] == pressed['bn']:
                for key in keySet['bn']:
                    keySet['fn']()
                    pk.press_key(key)
            else:
                for key in keySet['bn']:
                    pk.release_key(key)

    return mapped

# Convert to tuple?
def combineKeyAndWindow( o1 , o2 ):
    return { "window" : o1 , "keys" : o2 }

combined = i3CurrentWindow                        \
           .distinct_until_changed()              \
           .combine_latest( _keyPresses,
                            combineKeyAndWindow ) \
           .map( mapToPress )                     \

combined.subscribe()
