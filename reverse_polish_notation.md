There are two methods of defining how to use operators initially defined as strings:
- Defining the operator module: requires importing the operator module.
    import operator
    ops = {
             "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
             "/": operator.floordiv,
        }

- Using an anonymous function (lambda) to define operations:
    operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b,
        }

