from multiply import multi

def test_multiply_int():
    assert multi(2, 3) == 6

def test_multi_str():
    assert multi("a", 3) == "aaa"

def test_multi_empty():
    assert() == " "



