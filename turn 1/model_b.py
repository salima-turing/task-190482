import inspect
import unittest


class EmbeddedSystem:
    def __init__(self):
        self.register = 0

    def set_register(self, value):
        if value < 0 or value > 255:
            raise ValueError("Register value must be between 0 and 255")
        self.register = value

    def get_register(self):
        return self.register


class TestEmbeddedSystem(unittest.TestCase):
    def setUp(self):
        self.system = EmbeddedSystem()

    # **Traditional Test Method**
    def test_set_register_valid_value(self):
        self.system.set_register(100)
        self.assertEqual(self.system.get_register(), 100)

    # **Using Reflection for Dynamic Test Generation**
    def generate_test_functions_for_set_register(self):
        for test_data in [(0, 0), (255, 255), (-1, ValueError), (256, ValueError)]:
            input_value, expected_output = test_data

            def test_func(self):
                if isinstance(expected_output, type) and issubclass(expected_output, Exception):
                    with self.assertRaises(expected_output):
                        self.system.set_register(input_value)
                else:
                    self.system.set_register(input_value)
                    self.assertEqual(self.system.get_register(), expected_output)

            test_func.__name__ = f"test_set_register_{input_value}"
            setattr(self, test_func.__name__, test_func)


if __name__ == "__main__":
    # Generate test functions dynamically
    test_case = TestEmbeddedSystem()
    test_case.generate_test_functions_for_set_register()
    unittest.main()
