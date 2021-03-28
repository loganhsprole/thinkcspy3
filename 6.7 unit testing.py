import sys


# def test(did_pass):
#     """Print the result of a test."""
#     linenum = sys._getframe(1).f_lineno
#     if did_pass:
#         msg = "Test at line {0} ok.".format(linenum)
#     else:
#         msg = "Test at line {0} FAILED.".format(linenum)
#     print(msg)


def test_block():
    """Run the block of tests for code in this module (this file)."""
    assert absolute_value(17) == 17
    assert absolute_value(-17) == 17
    assert absolute_value(0) == 0
    assert absolute_value(3.14) == 3.14
    assert absolute_value(-3.14) == 3.14


# def absolute_value(x):
#     """Determine the absolute value of x"""
#     if x < 0:
#         return -x
#     return x


def absolute_value(x):  # bugged
    """Determine the absolute value of x (bugged)"""
    if x < 0:
        return 1
    elif x > 0:
        return x


# assert absolute_value(17) == 17

test_block()
