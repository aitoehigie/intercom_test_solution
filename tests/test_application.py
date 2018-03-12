#! /usr/bin/env python3

import pytest
from application import distance_calculator
from application import INTERCOM_LATITUDE, INTERCOM_LONGITUDE


def test_distance_calculator():
    assert distance_calculator(
        INTERCOM_LATITUDE, INTERCOM_LONGITUDE, 54.133333, -6.433333) == 89.03
    assert distance_calculator(
        INTERCOM_LATITUDE, INTERCOM_LONGITUDE, 54.180238, -5.920898) == 96.08


def test_distance_calculator_raises_exception_on_non_float_or_integer_arguments():
    with pytest.raises(TypeError):
        distance_calculator("jibberish")


def test_distance_calculator_raises_exception_on_zero_or_incomplete_arguments():
    with pytest.raises(TypeError):
        distance_calculator(INTERCOM_LATITUDE, INTERCOM_LONGITUDE, 54.133333)
        distance_calculator()
