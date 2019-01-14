from pykeyboard import PyKeyboard
pk = PyKeyboard()

do_nothing = lambda: None


baseKeys = [{ "bn": [ None ],                "fn" : do_nothing },
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
