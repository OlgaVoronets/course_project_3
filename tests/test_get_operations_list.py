import os
from src.utils import get_operations_list

def test_get_list():
    dir_ = os.path.dirname(__file__)
    file_path = os.path.join(dir_, 'test.json')
    assert get_operations_list(file_path) == [1, 2, 3]


