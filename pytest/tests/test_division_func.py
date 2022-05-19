from pytest.root_files.test1 import division


def test_division_good():
    assert division(10, 2) == 5

# print(division(10, 2))

# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(4) == 5
