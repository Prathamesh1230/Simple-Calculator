import math
from operators import safe_eval

class ExpressionEvaluator:
    def evaluate(self, expression):
        try:
            return safe_eval(expression)
        except Exception as e:
            return f"Error: {str(e)}"
