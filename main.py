import ast
import textwrap

import libcst as cst
from libcst.metadata import PositionProvider


def f():
    print("f")


def g():
    print("g")


def default():
    print("default")

# 1.1 dictを使った分岐
_switch_dict = {
    0: f,
    1: g,
    2: g,
    3: f,
    4: g,
}


def switch_dict_example(x):
    do_next = _switch_dict.get(x, default)
    do_next()

# 1.2 matchを使った分岐
def match_int_example(x):
    match x:
        case 0:
            f()
        case 1 | 2:
            g()
        case 3:
            f()
        case _:
            default()

# 1.3 ifを使った分岐
def match_int_elif_example(x):
    if x == 0:
        f()
    elif x in (1, 2):
        g()
    elif x == 3:
        f()
    else:
        default()


