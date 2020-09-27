import pytest

from gitremote.whats_my_name import my_name_is


def test_my_name_is():
    assert "Eugene Zuckerberg" == my_name_is()