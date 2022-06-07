from pytest.root_files.division import division
import pytest

@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 2, 10),
                                                   (30, -2, -15),
                                                   (5, 2, 2.5),
                                                   (10.1, 2, 5.05)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result