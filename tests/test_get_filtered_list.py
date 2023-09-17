from src.utils import get_filtered_list

dict_list = [{'a': 1, 'b': 2, 'c': 3},
             {'a': 1, 'b': 4, 'c': 3},
             {'a': 1, 'b': 2, 'c': 3},
             {'a': 1, 'b': 5, 'c': 3}]

def test_get_filtered_list():
    assert get_filtered_list(dict_list, 'b', 2) == [{'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'c': 3}]
