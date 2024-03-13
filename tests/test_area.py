import pytest
from math import pi, pow, sqrt
from area import get_area


def test_get_area():

    assert get_area(2) == pi * pow(2,2)

    assert get_area(3, 4, 5) == 6

    assert get_area(2, 3, 4) == sqrt(9/2 * (9/2 - 2) * (9/2 - 3) * (9/2 - 4))

    with pytest.raises(ValueError):
        get_area(1, 2, 3)

    with pytest.raises(ValueError):
        get_area(1, 2)
