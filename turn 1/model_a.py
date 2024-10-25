import inspect

class EmbeddedSystem:
	def __init__(self):
		self.temperature_sensor = 0
		self.light_sensor = 0

	def read_temperature(self):
		self.temperature_sensor = 25
		return self.temperature_sensor

	def read_light(self):
		self.light_sensor = 100
		return self.light_sensor

def optimize_test_design(system):
	test_cases = {}

	for name, method in inspect.getmembers(system, inspect.isfunction):
		if name.startswith('read_'):
			test_name = f"test_{name}"
			test_cases[test_name] = lambda method=method: assert method() > 0

	return test_cases

if __name__ == "__main__":
	system = EmbeddedSystem()
	optimized_tests = optimize_test_design(system)

	for test_name, test_function in optimized_tests.items():
		print(f"Running test: {test_name}")
		test_function()
		print(f"Test {test_name} passed!\n")
