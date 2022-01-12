# Тестирование. Unit-тестирование
# Unit тесты призваны протестировать какую-то небольшую функциональность: функцию, класс или модуль
# Можно написать unit тексты к классу, чтобы проверять, все ли он делает корректно

# чтобы определить свой unit тест можно воспользоваться стандартной библиотекой модулей minitest
# и определить свой класс, который наследуется от TestCase из модуля unittest
import unittest


class TestPython(unittest.TestCase):

    # определяем функции, которые являются тестами - начинаются с test
    # внутри этого теста можно проверить какие-то условия
    def test_float_to_int_coercion(self):
        self.assertEqual(1, int(1.0))

    def test_get_empty_dict(self):
        self.assertIsNone({}.get("key"))

    def test_trueness(self):
        self.assertTrue(bool(10))

    def test_integer_division(self):
        self.assertIs(10 / 5, 2)