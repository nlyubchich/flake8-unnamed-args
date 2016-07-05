import ast
__version__ = '0.0.1'


class UnnamedArgsChecker(object):
    """Mutable default argument checker.

    Flake8 extension that alerts when a mutable type is used
    as an argument's default value.
    """
    name = 'flake-unnamed-args'
    version = __version__
    _error_tmpl = '{}: Too many unnamed arguments for function call'
    _code = 'E751'

    def __init__(self, tree, filename):
        self.tree = tree

    def run(self):
        """Check that no functions are a single if statement"""
        for stmt in ast.walk(self.tree):
            if isinstance(stmt, ast.Call):
                not_named_args = [arg for arg in stmt.args
                                  if not isinstance(arg, ast.Name)]
                # TODO: remove hardcoded args len
                if len(stmt.args) > 3 and not_named_args:
                    error_msg = self._error_tmpl.format(self._code)
                    yield stmt.lineno, stmt.col_offset, error_msg, type(self)
