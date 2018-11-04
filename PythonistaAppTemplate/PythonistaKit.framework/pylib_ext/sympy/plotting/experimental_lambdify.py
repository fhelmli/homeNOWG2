#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista
#import pythonista

""" rewrite of lambdify - This stuff is not stable at all.

It is for internal use in the new plotting module.
It may (will! see the Q'n'A in the source) be rewritten.

It's completely self contained. Especially it does not use lambdarepr.

It does not aim to replace the current lambdify. Most importantly it will never
ever support anything else than sympy expressions (no Matrices, dictionaries
and so on).
"""

from __future__ import print_function, division

import re
from sympy import Symbol, NumberSymbol, I, zoo, oo
from sympy.core.compatibility import exec_

#  We parse the expression string into a tree that identifies functions. Then
# we translate the names of the functions and we translate also some strings
# that are not names of functions (all this according to translation
# dictionaries).
#  If the translation goes to another module (like numpy) the
# module is imported and 'func' is translated to 'module.func'.
#  If a function can not be translated, the inner nodes of that part of the
# tree are not translated. So if we have Integral(sqrt(x)), sqrt is not
# translated to np.sqrt and the Integral does not crash.
#  A namespace for all this is generated by crawling the (func, args) tree of
# the expression. The creation of this namespace involves many ugly
# workarounds.
#  The namespace consists of all the names needed for the sympy expression and
# all the name of modules used for translation. Those modules are imported only
# as a name (import numpy as np) in order to keep the namespace small and
# manageable.

#  Please, if there is a bug, do not try to fix it here! Rewrite this by using
# the method proposed in the last Q'n'A below. That way the new function will
# work just as well, be just as simple, but it wont need any new workarounds.
#  If you insist on fixing it here, look at the workarounds in the function
# sympy_expression_namespace and in lambdify.

# Q: Why are you not using python abstract syntax tree?
# A: Because it is more complicated and not much more powerful in this case.

# Q: What if I have Symbol('sin') or g=Function('f')?
# A: You will break the algorithm. We should use srepr to defend against this?
#  The problem with Symbol('sin') is that it will be printed as 'sin'. The
# parser will distinguish it from the function 'sin' because functions are
# detected thanks to the opening parenthesis, but the lambda expression won't
# understand the difference if we have also the sin function.
# The solution (complicated) is to use srepr and maybe ast.
#  The problem with the g=Function('f') is that it will be printed as 'f' but in
# the global namespace we have only 'g'. But as the same printer is used in the
# constructor of the namespace there will be no problem.

# Q: What if some of the printers are not printing as expected?
# A: The algorithm wont work. You must use srepr for those cases. But even
# srepr may not print well. All problems with printers should be considered
# bugs.

# Q: What about _imp_ functions?
# A: Those are taken care for by evalf. A special case treatment will work
# faster but it's not worth the code complexity.

# Q: Will ast fix all possible problems?
# A: No. You will always have to use some printer. Even srepr may not work in
# some cases. But if the printer does not work, that should be considered a
# bug.

# Q: Is there same way to fix all possible problems?
# A: Probably by constructing our strings ourself by traversing the (func,
# args) tree and creating the namespace at the same time. That actually sounds
# good.

from sympy.external import import_module
import warnings

#TODO debuging output


class vectorized_lambdify(object):
    """ Return a sufficiently smart, vectorized and lambdified function.

    Returns only reals.

    This function uses experimental_lambdify to created a lambdified
    expression ready to be used with numpy. Many of the functions in sympy
    are not implemented in numpy so in some cases we resort to python cmath or
    even to evalf.

    The following translations are tried:
      only numpy complex
      - on errors raised by sympy trying to work with ndarray:
          only python cmath and then vectorize complex128

    When using python cmath there is no need for evalf or float/complex
    because python cmath calls those.

    This function never tries to mix numpy directly with evalf because numpy
    does not understand sympy Float. If this is needed one can use the
    float_wrap_evalf/complex_wrap_evalf options of experimental_lambdify or
    better one can be explicit about the dtypes that numpy works with.
    Check numpy bug http://projects.scipy.org/numpy/ticket/1013 to know what
    types of errors to expect.
    """
    def __init__(self, args, expr):
        self.args = args
        self.expr = expr
        self.lambda_func = experimental_lambdify(args, expr, use_np=True)
        self.vector_func = self.lambda_func
        self.failure = False

    def __call__(self, *args):
        np = import_module('numpy')
        np_old_err = np.seterr(invalid='raise')
        try:
            temp_args = (np.array(a, dtype=np.complex) for a in args)
            results = self.vector_func(*temp_args)
            results = np.ma.masked_where(
                                np.abs(results.imag) > 1e-7 * np.abs(results),
                                results.real, copy=False)
        except Exception as e:
            #DEBUG: print 'Error', type(e), e
            if ((isinstance(e, TypeError)
                 and 'unhashable type: \'numpy.ndarray\'' in str(e))
                or
                (isinstance(e, ValueError)
                 and ('Invalid limits given:' in str(e)
                      or 'negative dimensions are not allowed' in str(e)  # XXX
                      or 'sequence too large; must be smaller than 32' in str(e)))):  # XXX
                # Almost all functions were translated to numpy, but some were
                # left as sympy functions. They recieved an ndarray as an
                # argument and failed.
                #   sin(ndarray(...)) raises "unhashable type"
                #   Integral(x, (x, 0, ndarray(...))) raises "Invalid limits"
                #   other ugly exceptions that are not well understood (marked with XXX)
                # TODO: Cleanup the ugly special cases marked with xxx above.
                # Solution: use cmath and vectorize the final lambda.
                self.lambda_func = experimental_lambdify(
                    self.args, self.expr, use_python_cmath=True)
                self.vector_func = np.vectorize(
                    self.lambda_func, otypes=[np.complex])
                results = self.vector_func(*args)
                results = np.ma.masked_where(
                                np.abs(results.imag) > 1e-7 * np.abs(results),
                                results.real, copy=False)
            else:
                # Complete failure. One last try with no translations, only
                # wrapping in complex((...).evalf()) and returning the real
                # part.
                if self.failure:
                    raise e
                else:
                    self.failure = True
                    self.lambda_func = experimental_lambdify(
                        self.args, self.expr, use_evalf=True,
                        complex_wrap_evalf=True)
                    self.vector_func = np.vectorize(
                        self.lambda_func, otypes=[np.complex])
                    results = self.vector_func(*args)
                    results = np.ma.masked_where(
                            np.abs(results.imag) > 1e-7 * np.abs(results),
                            results.real, copy=False)
                    warnings.warn('The evaluation of the expression is'
                            ' problematic. We are trying a failback method'
                            ' that may still work. Please report this as a bug.')
        finally:
            np.seterr(**np_old_err)

        return results


class lambdify(object):
    """Returns the lambdified function.

    This function uses experimental_lambdify to create a lambdified
    expression. It uses cmath to lambdify the expression. If the function
    is not implemented in python cmath, python cmath calls evalf on those
    functions.
    """

    def __init__(self, args, expr):
        self.args = args
        self.expr = expr
        self.lambda_func = experimental_lambdify(args, expr, use_evalf=True,
                                                 use_python_cmath=True)
        self.failure = False

    def __call__(self, args):
        args = complex(args)
        try:
            #The result can be sympy.Float. Hence wrap it with complex type.
            result = complex(self.lambda_func(args))
            if abs(result.imag) > 1e-7 * abs(result):
                return None
            else:
                return result.real
        except Exception as e:
            # The exceptions raised by sympy, cmath are not consistent and
            # hence it is not possible to specify all the exceptions that
            # are to be caught. Presently there are no cases for which the code
            # reaches this block other than ZeroDivisionError and complex
            # comparision. Also the exception is caught only once. If the
            # exception repeats itself,
            # then it is not caught and the corresponding error is raised.
            # XXX: Remove catching all exceptions once the plotting module
            # is heavily tested.
            if isinstance(e, ZeroDivisionError):
                return None
            elif isinstance(e, TypeError) and ('no ordering relation is'
                                               ' defined for complex numbers'
                                               in str(e)):
                self.lambda_func = experimental_lambdify(self.args, self.expr,
                                                         use_evalf=True,
                                                         use_python_math=True)
                result = self.lambda_func(args.real)
                return result
            else:
                if self.failure:
                    raise e
                #Failure
                #Try wrapping it with complex(..).evalf()
                self.failure = True
                self.lambda_func = experimental_lambdify(self.args, self.expr,
                                                    use_evalf=True,
                                                    complex_wrap_evalf=True)
                result = self.lambda_func(args)
                warnings.warn('The evaluation of the expression is'
                        ' problematic. We are trying a failback method'
                        ' that may still work. Please report this as a bug.')
                if abs(result.imag) > 1e-7 * abs(result):
                    return None
                else:
                    return result.real


def experimental_lambdify(*args, **kwargs):
    l = Lambdifier(*args, **kwargs)
    return l.lambda_func


class Lambdifier(object):
    def __init__(self, args, expr, print_lambda=False, use_evalf=False,
                 float_wrap_evalf=False, complex_wrap_evalf=False,
                 use_np=False, use_python_math=False, use_python_cmath=False,
                 use_interval=False):

        self.print_lambda = print_lambda
        self.use_evalf = use_evalf
        self.float_wrap_evalf = float_wrap_evalf
        self.complex_wrap_evalf = complex_wrap_evalf
        self.use_np = use_np
        self.use_python_math = use_python_math
        self.use_python_cmath = use_python_cmath
        self.use_interval = use_interval

        # Constructing the argument string
        if not all([isinstance(a, Symbol) for a in args]):
            raise ValueError('The arguments must be Symbols.')
        else:
            argstr = ', '.join([str(a) for a in args])

        # Constructing the translation dictionaries and making the translation
        self.dict_str = self.get_dict_str()
        self.dict_fun = self.get_dict_fun()
        exprstr = str(expr)
        newexpr = self.tree2str_translate(self.str2tree(exprstr))

        # Constructing the namespaces
        namespace = {}
        namespace.update(self.sympy_atoms_namespace(expr))
        namespace.update(self.sympy_expression_namespace(expr))
        # XXX Workaround
        # Ugly workaround because Pow(a,Half) prints as sqrt(a)
        # and sympy_expression_namespace can not catch it.
        from sympy import sqrt
        namespace.update({'sqrt': sqrt})
        # End workaround.
        if use_python_math:
            namespace.update({'math': __import__('math')})
        if use_python_cmath:
            namespace.update({'cmath': __import__('cmath')})
        if use_np:
            try:
                namespace.update({'np': __import__('numpy')})
            except ImportError:
                raise ImportError(
                    'experimental_lambdify failed to import numpy.')
        if use_interval:
            namespace.update({'imath': __import__(
                'sympy.plotting.intervalmath', fromlist=['intervalmath'])})
            namespace.update({'math': __import__('math')})

        # Construct the lambda
        if self.print_lambda:
            print(newexpr)
        eval_str = 'lambda %s : ( %s )' % (argstr, newexpr)
        exec_("from __future__ import division; MYNEWLAMBDA = %s" % eval_str, namespace)
        self.lambda_func = namespace['MYNEWLAMBDA']

    ##############################################################################
    # Dicts for translating from sympy to other modules
    ##############################################################################
    ###
    # builtins
    ###
    # Functions with different names in builtins
    builtin_functions_different = {
        'Min': 'min',
        'Max': 'max',
        'Abs': 'abs',
    }

    # Strings that should be translated
    builtin_not_functions = {
        'I': '1j',
        'oo': '1e400',
    }

    ###
    # numpy
    ###

    # Functions that are the same in numpy
    numpy_functions_same = [
        'sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh', 'exp', 'log',
        'sqrt', 'floor', 'conjugate',
    ]

    # Functions with different names in numpy
    numpy_functions_different = {
        "acos": "arccos",
        "acosh": "arccosh",
        "arg": "angle",
        "asin": "arcsin",
        "asinh": "arcsinh",
        "atan": "arctan",
        "atan2": "arctan2",
        "atanh": "arctanh",
        "ceiling": "ceil",
        "im": "imag",
        "ln": "log",
        "Max": "amax",
        "Min": "amin",
        "re": "real",
        "Abs": "abs",
    }

    # Strings that should be translated
    numpy_not_functions = {
        'pi': 'np.pi',
        'oo': 'np.inf',
        'E': 'np.e',
    }

    ###
    # python math
    ###

    # Functions that are the same in math
    math_functions_same = [
        'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2',
        'sinh', 'cosh', 'tanh', 'asinh', 'acosh', 'atanh',
        'exp', 'log', 'erf', 'sqrt', 'floor', 'factorial', 'gamma',
    ]

    # Functions with different names in math
    math_functions_different = {
        'ceiling': 'ceil',
        'ln': 'log',
        'loggamma': 'lgamma'
    }

    # Strings that should be translated
    math_not_functions = {
        'pi': 'math.pi',
        'E': 'math.e',
    }

    ###
    # python cmath
    ###

    # Functions that are the same in cmath
    cmath_functions_same = [
        'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
        'sinh', 'cosh', 'tanh', 'asinh', 'acosh', 'atanh',
        'exp', 'log', 'sqrt',
    ]

    # Functions with different names in cmath
    cmath_functions_different = {
        'ln': 'log',
        'arg': 'phase',
    }

    # Strings that should be translated
    cmath_not_functions = {
        'pi': 'cmath.pi',
        'E': 'cmath.e',
    }

    ###
    # intervalmath
    ###

    interval_not_functions = {
        'pi': 'math.pi',
        'E': 'math.e'
    }

    interval_functions_same = [
        'sin', 'cos', 'exp', 'tan', 'atan', 'log',
        'sqrt', 'cosh', 'sinh', 'tanh', 'floor',
        'acos', 'asin', 'acosh', 'asinh', 'atanh',
        'Abs', 'And', 'Or'
    ]

    interval_functions_different = {
        'Min': 'imin',
        'Max': 'imax',
        'ceiling': 'ceil',

    }

    ###
    # mpmath, etc
    ###
    #TODO

    ###
    # Create the final ordered tuples of dictionaries
    ###

    # For strings
    def get_dict_str(self):
        dict_str = dict(self.builtin_not_functions)
        if self.use_np:
            dict_str.update(self.numpy_not_functions)
        if self.use_python_math:
            dict_str.update(self.math_not_functions)
        if self.use_python_cmath:
            dict_str.update(self.cmath_not_functions)
        if self.use_interval:
            dict_str.update(self.interval_not_functions)
        return dict_str

    # For functions
    def get_dict_fun(self):
        dict_fun = dict(self.builtin_functions_different)
        if self.use_np:
            for s in self.numpy_functions_same:
                dict_fun[s] = 'np.' + s
            for k, v in self.numpy_functions_different.items():
                dict_fun[k] = 'np.' + v
        if self.use_python_math:
            for s in self.math_functions_same:
                dict_fun[s] = 'math.' + s
            for k, v in self.math_functions_different.items():
                dict_fun[k] = 'math.' + v
        if self.use_python_cmath:
            for s in self.cmath_functions_same:
                dict_fun[s] = 'cmath.' + s
            for k, v in self.cmath_functions_different.items():
                dict_fun[k] = 'cmath.' + v
        if self.use_interval:
            for s in self.interval_functions_same:
                dict_fun[s] = 'imath.' + s
            for k, v in self.interval_functions_different.items():
                dict_fun[k] = 'imath.' + v
        return dict_fun

    ##############################################################################
    # The translator functions, tree parsers, etc.
    ##############################################################################

    def str2tree(self, exprstr):
        """Converts an expression string to a tree.

        Functions are represented by ('func_name(', tree_of_arguments).
        Other expressions are (head_string, mid_tree, tail_str).
        Expressions that do not contain functions are directly returned.

        Examples:
        >>> from sympy.abc import x, y, z
        >>> from sympy import Integral, sin
        >>> from sympy.plotting.experimental_lambdify import Lambdifier
        >>> str2tree = Lambdifier([x], x).str2tree

        >>> str2tree(str(Integral(x, (x, 1, y))))
        ('', ('Integral(', 'x, (x, 1, y)'), ')')
        >>> str2tree(str(x+y))
        'x + y'
        >>> str2tree(str(x+y*sin(z)+1))
        ('x + y*', ('sin(', 'z'), ') + 1')
        >>> str2tree('sin(y*(y + 1.1) + (sin(y)))')
        ('', ('sin(', ('y*(y + 1.1) + (', ('sin(', 'y'), '))')), ')')
        """
        #matches the first 'function_name('
        first_par = re.search(r'(\w+\()', exprstr)
        if first_par is None:
            return exprstr
        else:
            start = first_par.start()
            end = first_par.end()
            head = exprstr[:start]
            func = exprstr[start:end]
            tail = exprstr[end:]
            count = 0
            for i, c in enumerate(tail):
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count == -1:
                    break
            func_tail = self.str2tree(tail[:i])
            tail = self.str2tree(tail[i:])
            return (head, (func, func_tail), tail)

    @classmethod
    def tree2str(cls, tree):
        """Converts a tree to string without translations.

        Examples:
        >>> from sympy.abc import x, y, z
        >>> from sympy import Integral, sin
        >>> from sympy.plotting.experimental_lambdify import Lambdifier
        >>> str2tree = Lambdifier([x], x).str2tree
        >>> tree2str = Lambdifier([x], x).tree2str

        >>> tree2str(str2tree(str(x+y*sin(z)+1)))
        'x + y*sin(z) + 1'
        """
        if isinstance(tree, str):
            return tree
        else:
            return ''.join(map(cls.tree2str, tree))

    def tree2str_translate(self, tree):
        """Converts a tree to string with translations.

        Function names are translated by translate_func.
        Other strings are translated by translate_str.
        """
        if isinstance(tree, str):
            return self.translate_str(tree)
        elif isinstance(tree, tuple) and len(tree) == 2:
            return self.translate_func(tree[0][:-1], tree[1])
        else:
            return ''.join([self.tree2str_translate(t) for t in tree])

    def translate_str(self, estr):
        """Translate substrings of estr using in order the dictionaries in
        dict_tuple_str."""
        for pattern, repl in self.dict_str.items():
                estr = re.sub(pattern, repl, estr)
        return estr

    def translate_func(self, func_name, argtree):
        """Translate function names and the tree of arguments.

        If the function name is not in the dictionaries of dict_tuple_fun then the
        function is surrounded by a float((...).evalf()).

        The use of float is necessary as np.<function>(sympy.Float(..)) raises an
        error."""
        if func_name in self.dict_fun:
            new_name = self.dict_fun[func_name]
            argstr = self.tree2str_translate(argtree)
            return new_name + '(' + argstr
        else:
            template = '(%s(%s)).evalf(' if self.use_evalf else '%s(%s'
            if self.float_wrap_evalf:
                template = 'float(%s)' % template
            elif self.complex_wrap_evalf:
                template = 'complex(%s)' % template
            return template % (func_name, self.tree2str(argtree))

    ##############################################################################
    # The namespace constructors
    ##############################################################################

    @classmethod
    def sympy_expression_namespace(cls, expr):
        """Traverses the (func, args) tree of an expression and creates a sympy
        namespace. All other modules are imported only as a module name. That way
        the namespace is not poluted and rests quite small. It probably causes much
        more variable lookups and so it takes more time, but there are no tests on
        that for the moment."""
        if expr is None:
            return {}
        else:
            funcname = str(expr.func)
            # XXX Workaround
            # Here we add an ugly workaround because str(func(x))
            # is not always the same as str(func). Eg
            # >>> str(Integral(x))
            # "Integral(x)"
            # >>> str(Integral)
            # "<class 'sympy.integrals.integrals.Integral'>"
            # >>> str(sqrt(x))
            # "sqrt(x)"
            # >>> str(sqrt)
            # "<function sqrt at 0x3d92de8>"
            # >>> str(sin(x))
            # "sin(x)"
            # >>> str(sin)
            # "sin"
            # Either one of those can be used but not all at the same time.
            # The code considers the sin example as the right one.
            regexlist = [
                r'<class \'sympy[\w.]*?.([\w]*)\'>$',
                # the example Integral
                r'<function ([\w]*) at 0x[\w]*>$',    # the example sqrt
            ]
            for r in regexlist:
                m = re.match(r, funcname)
                if m is not None:
                    funcname = m.groups()[0]
            # End of the workaround
            # XXX debug: print funcname
            args_dict = {}
            for a in expr.args:
                if (isinstance(a, Symbol) or
                    isinstance(a, NumberSymbol) or
                        a in [I, zoo, oo]):
                    continue
                else:
                    args_dict.update(cls.sympy_expression_namespace(a))
            args_dict.update({funcname: expr.func})
            return args_dict

    @staticmethod
    def sympy_atoms_namespace(expr):
        """For no real reason this function is separated from
        sympy_expression_namespace. It can be moved to it."""
        atoms = expr.atoms(Symbol, NumberSymbol, I, zoo, oo)
        d = {}
        for a in atoms:
            # XXX debug: print 'atom:' + str(a)
            d[str(a)] = a
        return d
