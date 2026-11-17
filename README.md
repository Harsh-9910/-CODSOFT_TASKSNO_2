# 🧮 Task 2: Calculator

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-Command--Line-blue)

A simple calculator that asks for two numbers and an operation, performs the calculation and shows the result.

## 📌 Features

- Takes two numbers (integers or decimals) and one operation as input
- Supports six operations (see the table below)
- Keeps asking until a valid number is entered, so it never crashes on bad input
- Handles division and modulus by zero with a clear error message
- Lets you do several calculations in one session

## ➗ Supported Operations

| Symbol | Operation | Example |
|--------|-----------|---------|
| `+` | Addition | `5 + 3 = 8` |
| `-` | Subtraction | `5 - 3 = 2` |
| `*` | Multiplication | `5 * 3 = 15` |
| `/` | Division | `10 / 4 = 2.5` |
| `%` | Modulus (remainder) | `10 % 3 = 1` |
| `**` | Exponent (power) | `2 ** 3 = 8` |

## ▶️ How to Run

```bash
python task2_calculator.py
```

No external libraries are required.

## 🖥️ Example Session

```
===== SIMPLE CALCULATOR =====
Operations: +  -  *  /  %  **
Enter first number: 10
Enter second number: 4
Choose operation (+, -, *, /, %, **): /
Result: 10 / 4 = 2.5

Calculate again? (y/n): n
Goodbye!
```

### Error handling

```
Enter first number: 5
Enter second number: 0
Choose operation (+, -, *, /, %, **): /
Error: division by zero is not allowed
```

## 🧠 How It Works

| Function | Purpose |
|----------|---------|
| `get_number(prompt)` | Loops until the user enters a valid number (`float`) |
| `calculate(a, b, op)` | Applies the chosen operation; returns an error message for zero division or `None` for an unknown operation |
| `main()` | Collects input, shows the result and asks whether to continue |

Results are displayed with the `:g` format so `2.0` appears as `2` and `2.5` stays `2.5`.

## 📚 Concepts Used

Functions, conditionals, `while` loops, `try`/`except`, string formatting (f-strings), input validation.

## 🔮 Ideas for Improvement

- Calculation history
- Chained expressions such as `2 + 3 * 4`
- A Tkinter GUI with buttons

