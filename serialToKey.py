import serial
import rx
from rx import Observable, Observer

#Port to listen on
port = '/dev/ttyACM0'

#Open connection to serial
_arduino = serial.Serial(port,9600,timeout=5)
_arduino.flush()

def listenForKeys(observer):
    while( True ):
        observer.on_next( _arduino.readline().decode('UTF-8').strip() )

def mapToBinary(buttonMap):
    return int(buttonMap.lstrip('0') or '0', 2)

_keyPresses = Observable                 \
              .create( listenForKeys )   \
              .distinct_until_changed()  \
              .map ( mapToBinary)        \


