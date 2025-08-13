class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

    def add(self, a: float, b: float) -> float:
        return a + b

calc = Calculator()

print("-" * 20)
print(f"\nSum of integers 5 and 10: {calc.add(5, 10)}\n")
print("-" * 20)
print(f"\nSum of floats 5.5 and 10.2: {calc.add(5.5, 10.2)}\n")
print("-" * 20)
