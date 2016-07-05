import ast
from unittest import TestCase
from unnamed_args import UnnamedArgsChecker


BAD_CALL = """
def func(a, b, c, d):
    return 1

func(1, 2, 3, 4)
"""

BAD_CALL_WITH_ATTRS = """
def func(a, b, c, d):
    return 1

class Cls:
    test1 = 1
    test2 = 2
    test3 = 3
    test4 = 4

func(Cls.test1, Cls.test2, Cls.test3, Cls.test4)
"""

GOOD_CALL = """
def func(a, b, c, d):
    return 1
a = 1
b = 2
c = 3
d = 4

func(a, b, c, d)
"""


class UnnamedArgsCheckedTestCase(TestCase):
    def test_blah(self):
        ast_tree = ast.parse(BAD_CALL)
        result = list(UnnamedArgsChecker(ast_tree, None).run())
        self.assertEqual(len(result), 1, 'Checker returns false negative')

    def test_clazz(self):
        ast_tree = ast.parse(BAD_CALL_WITH_ATTRS)
        result = list(UnnamedArgsChecker(ast_tree, None).run())
        self.assertEqual(len(result), 1, 'Checker returns false negative')

    def test_good(self):
        ast_tree = ast.parse(GOOD_CALL)
        result = list(UnnamedArgsChecker(ast_tree, None).run())
        self.assertEqual(len(result), 0, 'Checker returns false positive')
