from pytest.root_files.addition import addition


def test_addition_good():
    assert addition(10, 2) == 12