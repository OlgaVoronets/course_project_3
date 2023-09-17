from src.utils import hide_number

def test_hide_number():
    assert hide_number('12345678912345678912') == '**8912'
    assert hide_number('1234567891234567') == '1234 56** **** 4567'
