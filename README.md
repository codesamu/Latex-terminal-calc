# LaTeX Terminal Calculator

<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge" alt="Python Badge" />
<img src="https://img.shields.io/badge/SymPy-Symbolic%20Math-brightgreen?logo=sympy&logoColor=white&style=for-the-badge" alt="SymPy Badge" />
<img src="https://img.shields.io/badge/LaTeX-Math%20Input-8B3FFD?logo=latex&logoColor=white&style=for-the-badge" alt="LaTeX Badge" />

A terminal-based calculator that accepts mathematical equations in LaTeX-style input, parses them, and evaluates the result. This tool is ideal for students, engineers, and anyone who prefers writing math in LaTeX syntax.

## Features
- **LaTeX-style Input:** Enter math expressions using familiar LaTeX commands.
- **Fractions:** `\frac{a}{b}` → `a/b`
- **Exponents:** `x^{n}` or `x^n` → `x**n`
- **Square Roots:** `\sqrt{a}` → `math.sqrt(a)`
- **Integrals:**
  - Definite: `\int_{a}^{b} f(x) dx` → definite integral
  - Indefinite: `\int f(x) dx` → indefinite integral
- **Greek Symbols:** Supports `\omega`, `\pi`, `\alpha`, `\beta`, `\theta` as variables/constants
- **Standard Math Operations:** Addition, subtraction, multiplication, division, etc.
- **Safe Evaluation:** Uses `sympy` and `math` for symbolic and numeric calculations.

## Requirements
- Python 3.7+
- [SymPy](https://www.sympy.org/): Install with `pip install sympy`

## Usage
1. Run the calculator:
   ```bash
   python3 latex_terminal_calc.py
   ```
2. Enter a LaTeX math expression at the prompt. Examples:
   - `\frac{1}{2} + 3`
   - `2^{3} + \sqrt{16}`
   - `\int_{0}^{1} x^2 dx`
   - `\omega + \pi`
3. Type `exit` or `quit` to leave the calculator.

## Example
```
> \frac{1}{2} + 3
= 3.5
> \int_{0}^{1} x^2 dx
= 1/3
> \omega + 2
= omega + 2
```