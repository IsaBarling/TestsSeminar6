"""
This module contains the ListComparator class for comparing the averages of two lists.
"""


class ListComparator:
    """
    A class for comparing the averages of two lists.
    """

    @staticmethod
    def calculate_average(lst):
        """
        Calculate the average of a list.
        If the list is empty, return 0.
        """
        if not lst:
            return 0
        return sum(lst) / len(lst)

    @staticmethod
    def compare_averages(lst1, lst2):
        """
        Compare the averages of two lists and return a message indicating
        which list has a greater average or if the averages are equal.
        """
        avg1 = ListComparator.calculate_average(lst1)
        avg2 = ListComparator.calculate_average(lst2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        if avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
