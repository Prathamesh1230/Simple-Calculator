from evaluator import ExpressionEvaluator

def test_expressions():
    evaluator = ExpressionEvaluator()
    tests = {
        "2 + 3": 5,
        "10 - 4": 6,
        "3 * 5": 15,
        "10 / 2": 5,
        "2 ** 3": 8,
        "sqrt(16)": 4.0
    }
    for expr, expected in tests.items():
        result = evaluator.evaluate(expr)
        assert round(float(result), 2) == expected, f"Failed on {expr}"
    print("All tests passed!")

if __name__ == "__main__":
    test_expressions()
