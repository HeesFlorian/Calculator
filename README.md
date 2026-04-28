Scientific Calculator (CLI + GUI)

A modular scientific calculator written in Python.
The project includes both a command-line interface (CLI) and a graphical user interface (GUI).

It supports basic arithmetic operations as well as advanced mathematical functions like trigonometry, logarithms, and factorials.

Features:
- Basic operations: addition, subtraction, multiplication, division
- Advanced math: power, square root, logarithm
- Trigonometric functions: sin, cos, tan
- Error handling (e.g. division by zero)
- Modular structure
- CLI interface
- GUI (in process)

Planned additions:
- Function plotting
- Expression parsing

Uses:
- Python 3.13
- math module

Project Structure:
calculator/
|── include
|    |── operations.py
|    |── GUI.py
|
|── main.py
|── cli.py

How to run:
CLI version:
python cli.py

Example Usage:
Select operation:
1. Add
2. Subtract

Input1: 1
Input2: 2 2
Output: 4


GUI version: (NOT IMPLEMENTED)
python main.py

Author
Florian Hees
