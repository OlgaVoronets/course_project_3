import pytest
from src.utils import get_formatted_date


@pytest.mark.parametrize('date, expected', [("2019-08-26T10:50:58.294041", '26.08.2019'),
("2019-07-03T18:35:29.512364", '03.07.2019'), ("2018-06-30T02:08:58.425572", '30.06.2018')])
def test_get_formatted_date(date, expected):
    assert get_formatted_date(date) == expected