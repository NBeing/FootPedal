#!/usr/bin/python2
import serial
import syslog
import time
import pyautogui
import rx
import io
from time import sleep
from rx import Observable, Observer
from pykeyboard import PyKeyboard
from datetime import datetime

pk = PyKeyboard()

#Port to listen on
port = '/dev/ttyACM0'
#Open connection to serial
_arduino = serial.Serial(port,9600, timeout=5)
_arduino.flush()
time.sleep(2)

#List of keys for buttons 1,2,3,4
#keyList      = [ ['Up'],['Down'], [pk.control_key], [pk.alt_key]] 
#Drums Keylist
keyList = [ 'g', 'a', 'b', 'm' , 'g', 'a', 'b', 'm', 'g', 'a', 'b', 'm', 'g', 'a', 'b', 'm' ]

def now():
    return  datetime.now()

def listenForKeys(observer):
   while( True ):
        msg = _arduino.readline().decode('UTF-8').strip()
        observer.on_next(msg)

def mapToKey( keyMap ):
    print("mapToKey", keyMap, len(keyMap))

    [print (i,k) for i, k in  enumerate(keyMap)]
    mapped = [{
        'button' : i,
        'on'     : keyMap[i] ,
        'key'    : keyList[i],
        'last'   : now()
    } for i, k in enumerate(keyMap)]
    print (mapped)
    return mapped

def mapToPress(mapped):
    # print("Map to press")
    for k in mapped:
        if k['on'] == '1':
            for k in k['key']:
                print("pressing", k)
                pk.press_key(k)
        else:
            for k in k['key']:
                pk.release_key(k)

    return mapped

class ButtonObserver(Observer):
    def on_next(self, value):
        # print("===================================")
        # print("Vallue 2", value)
        return value

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))

source = Observable.create(listenForKeys)
source \
    .distinct_until_changed() \
    .map       ( lambda s: mapToKey      (s)) \
    .map       ( lambda s: mapToPress    (s)) \
    .subscribe ( ButtonObserver()           )

# Turns out I couldn't press the foot pedals fast enough to need a debounce

# def millis_interval(start, end):
#     """start and end are datetime instances"""
#     diff   =  end - start
#     millis =  diff.days * 24 * 60 * 60 * 1000
#     millis += diff.seconds * 1000
#     millis += diff.microseconds / 1000
#     return millis

# def toMillis( pressTime ):
#     """ Get the time difference from the last press"""
#     diffM = millis_interval(pressTime,now())
#     return diffM

# def setLastPress( ons, debounceList ):
#     debounceL = [ debounceList[i]
#                   for i, k in enumerate(ons)]
#     debounceList = debounceL
#     print("DB", debounceList)
#     return ons
# def debounce( presses, debounceList ):
    # Seems redundant, should just add the
    # debounce property
    # If time since the last press is more than 2 seconds then return
    # debounceListLast = [{ 'button'  : p['button'],
    #                       'key'     : p['key'],
    #                       'debounce': toMillis(debounceList[p['button']]) > 2000}
    #                     for i, p in enumerate(presses)]
    # return debounceListLast
