import unittest
import datetime
from lab5.date_utils import get_current_date, add_days_to_date, format_date, calculate_date_difference, is_leap_year


class TestDateUtilsFunctions(unittest.TestCase):
    def test_get_current_date(self):
        current_date = get_current_date()
        self.assertIsInstance(current_date, datetime.date)

    def test_add_days_to_date(self):
        base_date = datetime.date(2023, 1, 1)
        result_date = add_days_to_date(base_date, 5)
        self.assertEqual(result_date, datetime.date(2023, 1, 6))

    def test_format_date(self):
        date_to_format = datetime.date(2023, 1, 15)
        formatted_date = format_date(date_to_format, "%Y-%m-%d")
        self.assertEqual(formatted_date, "2023-01-15")

    def test_calculate_date_difference(self):
        date1 = datetime.date(20235, 1, 15)
        date2 = datetime.date(2023, 1, 10)
        difference = calculate_date_difference(date1, date2)
        self.assertEqual(difference, datetime.timedelta(days=5))

    def test_is_leap_year(self):
        leap_year = 2024
        non_leap_year = 2023
        self.assertTrue(is_leap_year(leap_year))
        self.assertFalse(is_leap_year(non_leap_year))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDateUtilsFunctions)
    result = unittest.TextTestRunner().run(suite)

    if result.wasSuccessful():
        print("Тесты выполнены успешно.")
    else:
        print("Ошибка в тестах. Пожалуйста, проверьте реализацию функций.")