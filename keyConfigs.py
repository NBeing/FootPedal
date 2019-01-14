from pykeyboard import PyKeyboard
pk = PyKeyboard()
import buttonMappings.baseKeys

do_nothing = lambda: None
ctrl = pk.control_key
alt  = pk.alt_key
supe = pk.super_l_key
hype = pk.hyper_l_key

baseKeys = [{ "bn": [''],                "fn" : do_nothing },
            { "bn": [ctrl],              "fn" : do_nothing },
            { "bn": [alt],               "fn" : do_nothing },
            { "bn": ['d'],               "fn" : do_nothing },
            { "bn": [supe],              "fn" : do_nothing },
            { "bn": ['e'],               "fn" : do_nothing },
            { "bn": ['f'],               "fn" : do_nothing },
            { "bn": ['g'],               "fn" : do_nothing },
            { "bn": [hype],              "fn" : do_nothing },
            { "bn": ['i'],               "fn" : do_nothing },
            { "bn": ['k'],               "fn" : do_nothing },
            { "bn": ['l'],               "fn" : do_nothing },
            { "bn": ['m'],               "fn" : do_nothing },
            { "bn": ['n'],               "fn" : do_nothing },
            { "bn": ['o'],               "fn" : do_nothing },
            { "bn": ['p'],               "fn" : do_nothing }]

emacsKeys = [{ "bn": [''],                 "fn" : do_nothing }, # 0000
             { "bn": [ctrl],               "fn" : do_nothing }, # 0001
             { "bn": [alt],                "fn" : do_nothing }, # 0010
             { "bn": ['y'],                "fn" : do_nothing }, # 0011
             { "bn": [supe],               "fn" : do_nothing }, # 0100
             { "bn": ['x'],                "fn" : do_nothing }, # 0101
             { "bn": [ctrl, '9'],          "fn" : do_nothing }, # 0110
             { "bn": [''],                 "fn" : do_nothing }, # 0111
             { "bn": [ctrl, 'g'],          "fn" : do_nothing }, # 1000
             { "bn": [ctrl, 'x', 'Right'], "fn" : do_nothing }, # 1001
             { "bn": [ctrl, 'x', 'Left'],  "fn" : do_nothing }, # 1010
             { "bn": [''],                 "fn" : do_nothing }, # 1011
             { "bn": [supe, '7'],          "fn" : do_nothing }, # 1101
             { "bn": [''],                 "fn" : do_nothing }, # 1100
             { "bn": [''],                 "fn" : do_nothing }, # 1110
             { "bn": [''],                 "fn" : do_nothing }] # 1111

termKeys = [{ "bn": [''],                "fn" : do_nothing },
            { "bn": [pk.control_key],    "fn" : do_nothing },
            { "bn": [pk.alt_key],        "fn" : do_nothing },
            { "bn": ['d'],               "fn" : do_nothing },
            { "bn": [pk.super_l_key],    "fn" : do_nothing },
            { "bn": ['e'],               "fn" : do_nothing },
            { "bn": ['f'],               "fn" : do_nothing },
            { "bn": ['g'],               "fn" : do_nothing },
            { "bn": [pk.hyper_l_key],    "fn" : do_nothing },
            { "bn": ['i'],               "fn" : do_nothing },
            { "bn": ['k'],               "fn" : do_nothing },
            { "bn": ['l'],               "fn" : do_nothing },
            { "bn": ['m'],               "fn" : do_nothing },
            { "bn": ['n'],               "fn" : do_nothing },
            { "bn": ['o'],               "fn" : do_nothing },
            { "bn": ['p'],               "fn" : do_nothing }]

keyConfigs = [{ "app": "Emacs24",        "config" : emacsKeys },
              { "app": "default",        "config" : baseKeys  },
              { "app": "Gnome-terminal", "config" : termKeys  }]
