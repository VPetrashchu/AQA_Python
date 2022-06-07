#from root_files.division import division

from nose.tools import raises


def division(a, b):
    return a / b


def test_division_good():
    assert division(10, 2) == 5


#@raises(TypeError, ValueError)
# def test_raises_type_error():
#   raise TypeError("This test passes")
