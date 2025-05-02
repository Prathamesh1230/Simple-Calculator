import math

def safe_eval(expr):
    allowed_names = {
        k: v for k, v in math.__dict__.items() if not k.startswith("__")
    }
    allowed_names.update({
        "abs": abs,
        "round": round,
        "pow": pow
    })
    return eval(expr, {"__builtins__": None}, allowed_names)
