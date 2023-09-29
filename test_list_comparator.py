import pytest
from ListComparator import ListComparator


def test_calculate_average():
    assert ListComparator.calculate_average([1, 2, 3, 4]) == 2.5
    assert ListComparator.calculate_average([]) == 0


def test_compare_averages():
    assert ListComparator.compare_averages([1, 2, 3, 4], [1, 2]) == "Первый список имеет большее среднее значение"
    assert ListComparator.compare_averages([1, 2], [1, 2, 3, 4]) == "Второй список имеет большее среднее значение"
    assert ListComparator.compare_averages([1, 2, 3, 4], [1, 2, 3, 4]) == "Средние значения равны"
