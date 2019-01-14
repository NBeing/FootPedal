#!/usr/bin/python

import rx # Could do more qualified import here

from rx              import Observable, Observer
from pykeyboard      import PyKeyboard
from i3CurrentWindow import i3CurrentWindow
from serialToKey     import _keyPresses
from keyConfigs      import do_nothing

pk = PyKeyboard()

def mapToKey( keyMap, keyList ):
    return keyList[keyMap]

def mapToPress(mapped):
    pressed = mapToKey(mapped['keys'], mapped['window'])

    for keySet in mapped['window']:
        if keySet['bn'] != ['']:
            if keySet['bn'] == pressed['bn']:
                for key in keySet['bn']:
                    keySet['fn']()
                    pk.press_key(key)
            else:
                for key in keySet['bn']:
                    for x in pressed['bn']:
                        if key == x:
                            do_nothing()
                        else:
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
