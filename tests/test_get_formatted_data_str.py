from src.utils import get_formatted_data_str


def test_get_formatted_data_str():
    assert get_formatted_data_str("MasterCard 7158300734726758") == 'MasterCard 7158 30** **** 6758'
    assert get_formatted_data_str("Счет 35383033474447895560") == 'Счет **5560'
    assert get_formatted_data_str(None) == 'Данные не указаны'