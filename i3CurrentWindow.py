import i3
import rx
from rx         import Observable, Observer
from keyConfigs import keyConfigs

tickTime = 400

def getI3CurrentWindow():
    for window in i3.filter(focused=True):
        return window['window_properties']['class']

def loadConfigBasedOnWindow(s):
    getKeyMapping = [ x for x in keyConfigs
                      if x['app'] == s ]
    newBinding = getKeyMapping if getKeyMapping else [x for x in keyConfigs if x['app'] == 'default']
    return newBinding[0]['config']

i3CurrentWindow = Observable                               \
                  .interval(tickTime)                      \
                  .map( lambda s: getI3CurrentWindow() ) \
                  .map( lambda s: loadConfigBasedOnWindow(s))
