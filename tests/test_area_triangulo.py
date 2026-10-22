from main import area_triangulo
from pytest import approx


def test_area_triangulo():
    actual_result = area_triangulo(102, 5)
    assert actual_result == approx(25, abs=0.01)