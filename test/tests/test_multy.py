from pytest.root_files.multy import multy


def test_multy_good():
    assert multy(10, 2) == 20
