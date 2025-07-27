import re
import math
from sympy import symbols, integrate, sympify, pi

def latex_to_python(expr):
    # Greek symbols mapping
    greek = {
        r'\\omega': 'omega',
        r'\\pi': 'pi',
        r'\\alpha': 'alpha',
        r'\\beta': 'beta',
        r'\\theta': 'theta',
        # Add more as needed
    }
    for latex, py in greek.items():
        expr = re.sub(latex, py, expr)
    # Convert \frac{a}{b} to (a)/(b)
    expr = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1)/(\2)', expr)
    # Convert ^{n} to **(n)
    expr = re.sub(r'\^\{([^{}]+)\}', r'**(\1)', expr)
    # Convert ^n to **n
    expr = re.sub(r'\^([a-zA-Z0-9]+)', r'**\1', expr)
    # Convert \sqrt{a} to math.sqrt(a)
    expr = re.sub(r'\\sqrt\{([^{}]+)\}', r'math.sqrt(\1)', expr)
    # Convert \int_{a}^{b} f(x) dx to integrate(f(x), (x, a, b))
    expr = re.sub(r'\\int_\{([^{}]+)\}\^\{([^{}]+)\} ([^ ]+) d([a-zA-Z])',
                  r'integrate(\3, (\4, \1, \2))', expr)
    # Convert \int f(x) dx to integrate(f(x), x)
    expr = re.sub(r'\\int ([^ ]+) d([a-zA-Z])', r'integrate(\1, \2)', expr)
    # Remove LaTeX whitespace
    expr = expr.replace(' ', '')
    return expr

def main():
    print("LaTeX Terminal Calculator (with integrals and Greek symbols)")
    print("Enter a LaTeX math expression (e.g., \\frac{1}{2} + 3, \\int_{0}^{1} x^2 dx, \\omega + 2):")
    # Define common symbols for sympy
    omega, alpha, beta, theta, x, y, z = symbols('omega alpha beta theta x y z')
    while True:
        try:
            latex_input = input('> ')
            if latex_input.lower() in {'exit', 'quit'}:
                break
            py_expr = latex_to_python(latex_input)
            # Evaluate the expression safely
            result = eval(py_expr, {"__builtins__": None, "math": math, "integrate": integrate, "sympify": sympify, "omega": omega, "alpha": alpha, "beta": beta, "theta": theta, "x": x, "y": y, "z": z, "pi": pi})
            print(f"= {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main() 