#import pythonista
from .boolalg import (to_cnf, to_dnf, And, Or, Not, Xor, Nand, Nor, Implies,
    Equivalent, ITE, POSform, SOPform, simplify_logic,
    bool_equal, bool_map, true, false)
from .inference import satisfiable
