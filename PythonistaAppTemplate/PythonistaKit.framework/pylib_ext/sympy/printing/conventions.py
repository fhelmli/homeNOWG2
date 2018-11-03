
"""
A few practical conventions common to all printers.
"""

from __future__ import print_function, division

import re
import collections


def split_super_sub(text):
    """Split a symbol name into a name, superscripts and subscripts

       The first part of the symbol name is considered to be its actual
       'name', followed by super- and subscripts. Each superscript is
       preceded with a "^" character or by "__". Each subscript is preceded
       by a "_" character.  The three return values are the actual name, a
       list with superscripts and a list with subscripts.

       >>> from sympy.printing.conventions import split_super_sub
       >>> split_super_sub('a_x^1')
       ('a', ['1'], ['x'])
       >>> split_super_sub('var_sub1__sup_sub2')
       ('var', ['sup'], ['sub1', 'sub2'])

    """
    pos = 0
    name = None
    supers = []
    subs = []
    while pos < len(text):
        start = pos + 1
        if text[pos:pos + 2] == "__":
            start += 1
        pos_hat = text.find("^", start)
        if pos_hat < 0:
            pos_hat = len(text)
        pos_usc = text.find("_", start)
        if pos_usc < 0:
            pos_usc = len(text)
        pos_next = min(pos_hat, pos_usc)
        part = text[pos:pos_next]
        pos = pos_next
        if name is None:
            name = part
        elif part.startswith("^"):
            supers.append(part[1:])
        elif part.startswith("__"):
            supers.append(part[2:])
        elif part.startswith("_"):
            subs.append(part[1:])
        else:
            raise RuntimeError("This should never happen.")

    # make a little exception when a name ends with digits, i.e. treat them
    # as a subscript too.
    m = re.match('(^[a-zA-Z]+)([0-9]+)$', name)
    if m is not None:
        name, sub = m.groups()
        subs.insert(0, sub)

    return name, supers, subs

def requires_partial(expr):
    """Return whether a partial derivative symbol is required for printing

    This requires checking how many free variables there are,
    filtering out the ones that are integers. Some expressions don't have
    free variables. In that case, check its variable list explicitly to
    get the context of the expression.
    """

    if not isinstance(expr.free_symbols, collections.Iterable):
        return len(set(expr.variables)) > 1

    return sum(not s.is_integer for s in expr.free_symbols) > 1
