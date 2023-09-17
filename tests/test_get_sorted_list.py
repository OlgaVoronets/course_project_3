from src.utils import get_sorted_list

data = [{"date": "2019-08-26T10:50:58.294041"}, {"date": "2019-07-03T18:35:29.512364"}, {"date": "2018-06-30T02:08:58.425572"}]


def test_get_sorted_list():
    assert get_sorted_list(data, 'date') == [{'date': "2019-08-26T10:50:58.294041"}, {'date': "2019-07-03T18:35:29.512364"}, {'date': "2018-06-30T02:08:58.425572"}]

